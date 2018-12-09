import collections

requirements_orig = collections.defaultdict(list)
jobs = set()
with open("input/day7.input") as input:
    for row in input:
        r = row.strip().split()
        requirements_orig[r[7]].append(r[1])
        jobs.add(r[1])
        jobs.add(r[7])

def find_available_sorted(jobs, requirements):
    available = []
    for j in jobs:
        if not j in requirements:
            available.append(j)
    return sorted(available)

def clean_requirements(job, requirements):
    clean = collections.defaultdict(list)
    for k, v in requirements.items():
        if len(v) != 0:
            for e in v:
                if e != job:
                    clean[k].append(e)
    return clean


requirements = dict(requirements_orig)
ordering = ""
all_jobs = set(jobs)
while True:
    available_jobs = find_available_sorted(all_jobs, requirements)
    if len(available_jobs) != 0:
        j = available_jobs[0]
        ordering += j
        requirements = clean_requirements(j, requirements)
        all_jobs.remove(j)
    else:
        break

print(ordering)

## Part 2

def get_duration(jobs):
    all_jobs = {}
    for j in jobs:
        all_jobs[j] = ord(j)-4
    return all_jobs


all_jobs_with_duration = get_duration(jobs)
free_workers = 5
working = []
requirements = dict(requirements_orig)
ordering = ""
counter = 0
print(all_jobs_with_duration)
while True:
    available_jobs = find_available_sorted(all_jobs_with_duration, requirements)

    remove_working = []
    for job in available_jobs:
        if not job in working:
            remove_working.append(job)

    available_jobs = remove_working

    for worker in range(0, free_workers):
        if len(available_jobs) != 0:
            working.append(available_jobs[0])
            available_jobs = available_jobs[1:]
            free_workers -= 1

    fresh_working = []

    for running_job in working:
        all_jobs_with_duration[running_job] -= 1
        if all_jobs_with_duration[running_job] == 0:
            ordering += running_job
            requirements = clean_requirements(running_job, requirements)
            all_jobs_with_duration.pop(running_job)
            free_workers+=1
        else:
            fresh_working.append(running_job)
    working = fresh_working

    counter += 1
    if len(all_jobs_with_duration) == 0:
        break

print(counter)
print(ordering)