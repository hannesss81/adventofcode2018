import tqdm, time
from blist import *

players, last_score = None, None

with open("input/day9.input") as input:
    for line in input:
        parts = line.strip().split()
        players, last_score = map(int, (parts[0], parts[6]))


def play_game(players, last_score):
    scores = [0 for _ in range(players)]
    table = blist([0])
    p, loc = 0, 1
    for c in tqdm.tqdm(range(1, last_score+1)):
        if c % 23 == 0:
            scores[p] += c
            loc = (loc-7) % len(table)
            if (loc-2 < 0):
                scores[p] += table.pop((loc-1) % len(table))
            else:
                scores[p] += table.pop((loc-2) % len(table))

        else:
            table.insert(loc, c)
            loc = (loc+2) % len(table)
        p = (p+1) % (players)
    return scores

# scores = play_game(players, last_score)
#
# time.sleep(1)
# print(max(scores))
# time.sleep(1)

scores = play_game(players, last_score*100)
# time.sleep(1)
print("Part2 2: {} ".format(max(scores)))
# time.sleep(1)
