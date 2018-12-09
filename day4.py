import time
import collections


log_data = []
with open("input/day4.input") as input:
    for row in input:
        t, msg = time.strptime(row[0:18], "[%Y-%m-%d %H:%M]"), row[18:].strip()
        log_data.append((t, msg))

log_data.sort(key=lambda x:x[0])

guards_data = collections.defaultdict(lambda: collections.defaultdict(list))


current_guard = None
for t, msg in log_data:
    day_key = t.tm_yday
    time_key = t.tm_min
    if msg[0] == "f":
        guards_data[current_guard][day_key].append((time_key,0))
    elif msg[0] == "w":
        guards_data[current_guard][day_key].append((time_key,1))
    else:
        current_guard = int(msg.split()[1][1:])
        if t.tm_hour != 23:
            guards_data[current_guard][day_key].append((time_key, 1))

guard_full_data = collections.defaultdict(lambda: collections.defaultdict(list))
for k, v in guards_data.items():
    guard_full_data[k]["sum"] = 0
    for day, timeline in v.items():
        full_timeline = []
        sleep_s, i, status  = 0, 0, 1
        for minute in range(0, 60):
            cur_timeline = timeline[i]
            if cur_timeline[0] == minute:
                if(i < len(timeline)-1):
                    i += 1
                status = cur_timeline[1]
            full_timeline.append(status)
            if status == 0:
                sleep_s += 1
        guard_full_data[k][day] = full_timeline
        guard_full_data[k]["sum"] += sleep_s

max = 0
id = None
for g in guard_full_data.items():
    if g[1]["sum"] > max:
        max = g[1]["sum"]
        id = g[0]

sleep_overlap = [0 for x in range(0,60)]
for key, value in guard_full_data[id].items():
    if key == "sum":
        continue
    for i, status in enumerate(value):
        sleep_overlap[i] += status

often_sleep_minute = sleep_overlap.index(min(sleep_overlap))
print(often_sleep_minute*id)

all_guards_sleep = []
for guard_id, data in guard_full_data.items():
    sleep_overlap = [0 for x in range(0, 60)]
    for day_id, value in data.items():
        if day_id == "sum":
            continue
        for i, status in enumerate(value):
            sleep_overlap[i] += status
    often_sleep_minute = sleep_overlap.index(min(sleep_overlap))
    all_guards_sleep.append([guard_id, len(data)-min(sleep_overlap), often_sleep_minute, guard_id*often_sleep_minute])

all_guards_sleep.sort(key=lambda x:x[1])
print(all_guards_sleep[-1])