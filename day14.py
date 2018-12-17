from blist import blist

class Elf:
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

elves = blist([Elf(0,0), Elf(1,1)])

recipes = blist([3,7])
limit = blist([5,4,0,5,6,1])

# l = None
# while l != limit + 10:
#     sum = 0
#
#     for elf in elves:
#         sum += recipes[elf.pos]
#     for n in str(sum):
#         recipes.append(int(n))
#
#     l = len(recipes)
#     for elf in elves:
#         elf.pos = (1 + elf.pos + recipes[elf.pos]) % l

#part 1
# print("".join(map(str,recipes[-10:])))

def subfinder(mylist, pattern):
    matches = blist([])
    for i in range(len(mylist)):
        if mylist[i] == pattern[0] and mylist[i:i+len(pattern)] == pattern:
            matches.append(pattern)
            print(i)
            return False
    return True

while subfinder(recipes, limit):
    sum = 0
    for elf in elves:
        sum += recipes[elf.pos]
    for n in str(sum):
        recipes.append(int(n))

    l = len(recipes)
    for elf in elves:
        elf.pos = (1 + elf.pos + recipes[elf.pos]) % l