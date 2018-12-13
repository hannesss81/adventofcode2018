import collections

state =  "##....#.#.#...#.#..#.#####.#.#.##.#.#.#######...#.##....#..##....#.#..##.####.#..........#..#...#"

rules = []
for line in open("input/day12.input"):
    rules.append(line.strip().split(" =>")[0])

def generate_tree(rules):
    tree = lambda: collections.defaultdict(tree)
    rules_tree = tree()
    for r in rules:
        c = r[2]
        l1, l2 = r[0], r[1]
        r1, r2 = r[4], r[3]
        rules_tree[c][l1][l2][r1][r2] = "ok"
    return rules_tree

tree = generate_tree(rules)

def matches(tree, p):
    c = p[2]
    l1, l2 = p[0], p[1]
    r1, r2 = p[4], p[3]
    if tree[c][l1][l2][r1][r2]:
        return True
    return False

limit = 21
generation = 0
prevsum = 1
while True:
    new_state = ""
    for i in range(len(state)+4):
        if (i<4):
            if matches(tree, (4-i)*"."+state[:i+1]):
                new_state += "#"
            else:
                new_state += "."
        elif (i>len(state)-2):
            if matches(tree, state[i-4:]+"."*(i-len(state)+1)):
                new_state += "#"
            else:
                new_state += "."
        else:
            if matches(tree, state[i-4:i+1]):
                new_state += "#"
            else:
                new_state += "."
    generation += 1
    state = new_state
    if(generation >= limit):
        break
        
    # if generation % 100 == 0:
    #     while state.startswith("...."):
    #         state = state[5:]
    #     while state.endswith("...."):
    #         state = state[:-5]
    
    if generation % 20 == 0:
        sum = 0
        for i, pot in enumerate(state):
            if pot == "#":
                sum += i-(2*generation)
        print(f"{generation}., {sum}")
        prevsum = sum
                
t_s = 43168
a = (50_000_000_000 - 1000)/1000
print(t_s + a*42000)
