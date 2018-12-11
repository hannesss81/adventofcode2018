
data = []

with open("day8.input") as input:
    for line in input:
        data += line.strip().split()

def traverse(data, status, sum = 0):
    if data:
        if status == "header":
            child_c = int(data.pop(0))
            metadata_c = int(data.pop(0))
            for _ in range(0, child_c):
                sum += traverse(data, "header")
            for _ in range(0, metadata_c):
                sum += traverse(data.pop(0), "metadata")
            return sum
        if status == "metadata":
            return int(data)
        
print(traverse(list(data), "header"))

def traverse_2(data, status, sum = 0):
    if data:
        if status == "header":
            child_c = int(data.pop(0))
            metadata_c = int(data.pop(0))
            meta_sums = []
            for _ in range(0, child_c):
                meta_sums.append(traverse_2(data, "header"))
            for _ in range(0, metadata_c):
                if child_c == 0:
                    sum += traverse(data.pop(0), "metadata")
                else:
                    cur_sum = traverse_2(data.pop(0), "metadata")
                    if cur_sum != 0 and len(meta_sums) >= cur_sum:
                        sum += meta_sums[cur_sum-1]     
            return sum
        if status == "metadata":
            return int(data)
     
print(traverse_2(list(data), "header"))