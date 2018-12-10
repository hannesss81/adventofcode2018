import re, math

data = []

with open("input/day10_test.input") as input:
    for line in input:
       m = map(int, re.findall("-?\d+", line.strip()))
       data.append(list(m))

area = math.inf
while True:
    minx, miny, maxx, maxy = math.inf, math.inf, -math.inf, -math.inf

    for i, each in enumerate(data):
        x, y, vecx, vecy = each
   
        #data[i][0] += vecx
        #data[i][1] += vecy

        minx = x if x < minx else minx
        miny = y if y < miny else miny
        maxx = x if x > maxx else maxx
        maxy = y if y > maxy else maxy
        
        data[i][0] += vecx
        data[i][1] += vecy
    
    new_area = (maxx-minx)*(maxy-miny)

    if new_area < area:
        area = new_area
    else:
        for i, each in enumerate(data):
            x, y, vecx, vecy = each
            data[i][0] -= vecx
            data[i][1] -= vecy
        break

h = maxy-miny
w = maxx-minx

print(minx,maxx)
print(miny,maxy)

matrix = [["." for _ in range(w)] for _ in range(h)]
for each in matrix:
    print("".join(each))

print(data)

for x, y, _, _ in data:
    print("a", x, y)
    matrix[x-h][y-w] = "#"

print(matrix)
