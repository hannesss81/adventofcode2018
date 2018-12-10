import re, math

data = []
with open("input/day10.input") as input:
    for line in input:
       m = map(int, re.findall("-?\d+", line.strip()))
       data.append(list(m))

area = math.inf
t = 0
while True:
    minx, miny, maxx, maxy = math.inf, math.inf, -math.inf, -math.inf

    for i, each in enumerate(data):
        x, y, vecx, vecy = each
        minx = x if x < minx else minx
        miny = y if y < miny else miny
        maxx = x if x > maxx else maxx
        maxy = y if y > maxy else maxy
    
    new_area = (maxx-minx)*(maxy-miny)
    if new_area < area:
        area = new_area
        prev_limits = (minx, miny, maxx, maxy)
    else:
        t -= 1
        for i, each in enumerate(data):
            x, y, vecx, vecy = each
            data[i][0] -= vecx
            data[i][1] -= vecy
        break
    for i, each in enumerate(data):
        x, y, vecx, vecy = each
        data[i][0] += vecx
        data[i][1] += vecy
    t += 1
        
minx, miny, maxy, maxy = prev_limits
h, w = maxx-minx+1, maxy-miny+1

matrix = [["." for _ in range(h)] for _ in range(w)]
for x, y, _, _ in data:
    real_x = abs(x - minx)
    real_y = abs(y - miny)
    matrix[real_y][real_x] = "#"
    
for each in matrix:
   print("".join(each))

print(t)
