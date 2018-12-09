import math, collections

coords = []


with open("input/day6.input") as input:
    max_x, max_y = 0, 0
    min_x, min_y = math.inf, math.inf
    for row in input:
        x, y = row.strip().split(",")
        x, y = int(x), int(y)
        min_x = x if x < min_x else min_x
        min_y = y if y < min_y else min_y
        max_x = x if x > max_x else max_x
        max_y = y if y > max_y else max_y
        coords.append((x,y))


borders = (min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)

print(borders)
print(coords)

def find_closest(i, j, coords):
    distances = []
    for x,y in coords:
        distances.append(abs(x-i) + abs(y-j))

    minimum_d = min(distances)
    indices = [i for i, v in enumerate(distances) if v == minimum_d]

    if len(indices) == 1:
        return indices[0]
    else:
        return "."

def remove_infinite(ids, coords, borders):
    kaput = set()
    for id, (x, y) in enumerate(coords):
        if (x == borders[0][0]) or (x == borders[2][0]):
            kaput.add(id)
        if (y == borders[0][1]) or (y == borders[3][1]):
            kaput.add(id)

    print(kaput)
    clean_ids = []
    for id in ids:
        if not id in kaput:
            clean_ids.append(id)
    return clean_ids

closest_counter = []
for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        id = find_closest(i,j, coords)
        closest_counter.append(id)

closest_counter = remove_infinite(closest_counter,coords, borders)

print(collections.Counter(closest_counter))

## Part 2

def find_all_sum(i, j, coords):
    distances = []
    for x,y in coords:
        distances.append(abs(x-i) + abs(y-j))
    return sum(distances)

limit = 10_000
total = 0

lucky_number = 0

for i in range(min_x-lucky_number, max_x+lucky_number):
    for j in range(min_y-lucky_number, max_y+lucky_number):
        s = find_all_sum(i, j, coords)
        total += 1 if s < limit else 0
print(total)

