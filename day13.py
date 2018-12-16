
class Cart:
    def __init__(self, i, j, dir):
        self.i = i
        self.j = j
        self.dir = dir
        self.cn = 0
    def __str__(self):
        return f"({self.i},{self.j})"
    def __repr__(self):
        return self.__str__()

grid = []

for line in open("input/day13_test.input"):
    grid.append([])
    for t in line.strip("\n"):
        grid[-1].append(t)

carts = []

def getbounds(grid, i, j):
    l, r, u, d = " ", " ", " ", " "

    if j-1 >= 0:
        l = grid[i][j-1]
    if i-1 >= 0 and j < len(grid[i-1]):
        u = grid[i-1][j]
    if i+1 < len(grid) and j < len(grid[i+1]):
        d = grid[i+1][j]
    if j+1 < len(grid[i]):
        r = grid[i][j+1]

    return l, r, u, d


for i in range(len(grid)):
    for j in range(len(grid[i])):
        t = grid[i][j]
        if t in "<>v^":
            carts.append(Cart(i, j, t))
            l,r,u,d = getbounds(grid, i,j)
            if (l == " " or l == "|" or l == "\\" or l == "/" or l == "v" or l == "^") and (r == " " or r == "|" or r == "\\" or r == "/" or r == "v" or r == "^"):
                grid[i][j] = "|"
            elif l == "-" and r == "-" or l == "+" or r == "+" or l == "\\" or l == "/" or r == "\\" or r == "/" or l == "<" or r == "<" or l == ">" or r == ">":
                grid[i][j] = "-"
            elif u == " ":
                if l == " ":
                    grid[i][j] = "/"
                elif r == " ":
                    grid[i][j] = "\\"
            elif d == " ":
                if l == " ":
                    grid[i][j] = "\\"
                elif r == " ":
                    grid[i][j] = "/"
            else:
                print("?")


tick = 0
while True:

    if len(carts) == 1:
        print(tick, carts)
        break

    cart_loc = []
    crash_site = []

    carts.sort(key=lambda x: (x.i, x.j))

    for cart in carts:
        cur = grid[cart.i][cart.j]
        old_loc = (cart.i, cart.j)

        l, r, u, d = getbounds(grid, cart.i, cart.j)

        if cur == "-":
            if cart.dir == ">":
                cart.j += 1
                if r == "\\":
                    cart.dir = "v"
                elif r == "/":
                    cart.dir = "^"
            elif cart.dir == "<":
                cart.j -= 1
                if l == "\\":
                    cart.dir = "^"
                elif l == "/":
                    cart.dir = "v"
        elif cur == "|":
            if cart.dir == "v":
                cart.i += 1
                if d == "\\":
                    cart.dir = ">"
                elif d == "/":
                    cart.dir = "<"
            elif cart.dir == "^":
                cart.i -= 1
                if u == "\\":
                    cart.dir = "<"
                elif u == "/":
                    cart.dir = ">"
        elif cur == "\\":
            if cart.dir == ">":
                cart.j += 1
            elif cart.dir == "<":
                cart.j -= 1
            elif cart.dir == "^":
                cart.i -= 1
            elif cart.dir == "v":
                cart.i += 1
        elif cur == "/":
            if cart.dir == ">":
                cart.j += 1
            elif cart.dir == "<":
                cart.j -= 1
            elif cart.dir == "^":
                cart.i -= 1
            elif cart.dir == "v":
                cart.i += 1
        elif cur == "+":
            if cart.cn % 3 == 0: ## Turn left
                if cart.dir == ">":
                    cart.i -= 1
                    if u == "\\":
                        cart.dir = "<"
                    elif u == "/":
                        cart.dir = ">"
                    else:
                        cart.dir = "^"
                elif cart.dir == "^":
                    cart.j -= 1
                    if l == "\\":
                        cart.dir = "^"
                    elif l == "/":
                        cart.dir = "v"
                    else:
                        cart.dir = "<"
                elif cart.dir == "<":
                    cart.i += 1
                    if d == "\\":
                        cart.dir = ">"
                    elif d == "/":
                        cart.dir = "<"
                    else:
                        cart.dir = "v"
                elif cart.dir == "v":
                    cart.j += 1
                    if r == "\\":
                        cart.dir = "v"
                    elif r == "/":
                        cart.dir = "^"
                    else:
                        cart.dir = ">"
            elif cart.cn % 3 == 1: ## Continue straight
                if cart.dir == ">":
                    cart.j += 1
                    if r == "/":
                        cart.dir = "^"
                    elif r == "\\":
                        cart.dir = "v"
                elif cart.dir == "^":
                    cart.i -= 1
                    if u == "/":
                        cart.dir = ">"
                    elif u == "\\":
                        cart.dir = "<"
                elif cart.dir == "<":
                    cart.j -= 1
                    if l == "/":
                        cart.dir = "v"
                    elif l == "\\":
                        cart.dir = "^"
                elif cart.dir == "v":
                    cart.i += 1
                    if d == "/":
                        cart.dir = "<"
                    elif d == "\\":
                        cart.dir = ">"
            elif cart.cn % 3 == 2: ## Turn right
                if cart.dir == ">":
                    cart.i += 1
                    if d == "\\":
                        cart.dir = ">"
                    elif d == "/":
                        cart.dir = "<"
                    else:
                        cart.dir = "v"
                elif cart.dir == "^":
                    cart.j += 1
                    if r == "\\":
                        cart.dir = "v"
                    elif r == "/":
                        cart.dir = "^"
                    else:
                        cart.dir = ">"
                elif cart.dir == "<":
                    cart.i -= 1
                    if u == "\\":
                        cart.dir = "<"
                    elif u == "/":
                        cart.dir = ">"
                    else:
                        cart.dir = "^"
                elif cart.dir == "v":
                    cart.j -= 1
                    if l == "\\":
                        cart.dir = "^"
                    elif l == "/":
                        cart.dir = "v"
                    else:
                        cart.dir = "<"
            cart.cn += 1


        if (cart.i, cart.j) in cart_loc or (old_loc[0], old_loc[1]) in cart_loc:
            crash_site.append((old_loc[0], old_loc[1]))
            crash_site.append((cart.i, cart.j))
        else:
            cart_loc.append((cart.i, cart.j))

    new_carts = []
    for cart in carts:
        if not (cart.i, cart.j) in crash_site:
            new_carts.append(cart)
    carts = new_carts

    tick += 1

