claims = []

with open("input/day3.input") as input:
    for line in input:
        claims.append(line.strip().split(" "))


def coords_to_ids(begin_x, begin_y, size_x, size_y):
    ids = []
    for i in range(0, size_y):
        row_begin_id = begin_y + i
        for j in range(0, size_x):
            ids.append(f"{row_begin_id},{begin_x+j}")
    return ids


## Part 1
grid = {}
claim_ids = set()

for claim in claims:
    claim_id = claim[0]
    begin_x, begin_y = claim[2][:-1].split(",")
    size_x, size_y = claim[3].split("x")
    for coord_id in coords_to_ids(int(begin_x), int(begin_y), int(size_x), int(size_y)):
        if coord_id in grid:
            grid[coord_id][1] += 1
            grid[coord_id][0].append(claim_id)
            continue
        grid[coord_id] = [[claim_id], 0]
    claim_ids.add(claim_id)

overlap_c = 0
for value in grid.values():
    if value[1] > 0:
        overlap_c += 1
        claim_ids -= set(value[0])  # Remove claim_id that has an overlap

print(overlap_c)

# Part 2
print(claim_ids)
