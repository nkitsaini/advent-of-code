from typing import *
import re
from functools import cmp_to_key
import math
from dataclasses import dataclass
from pprint import pprint
from collections import defaultdict
import tempfile

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

ans = 0

details = []
beacons = set()

while True:
    line = get_line()
    if line is None: break
    match = re.match('.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', line)
    sx =  int(match.group(1))
    sy =  int(match.group(2))
    bx =  int(match.group(3))
    by =  int(match.group(4))
    details.append(((sx, sy), (bx, by)))
    beacons.add((bx, by))

def dist(p1, p2) -> int:
    return abs(p1[0] -p2[0]) + abs(p1[1] - p2[1])


value_row = 10
max_idx = 20
max_idx = 4000000
visited = set()
ranges = []

def add_range(s, e):


# for (sx, sy), (bx, by) in details:
for value_row in range(0, max_idx + 1):
    print(value_row)
    for s, b in details:
        distance = dist(s, b)
        max_x = s[0] + distance
        min_x = s[0] - distance

        for x in range(min_x, max_x + 1):
            if dist(s, (x, value_row)) <= distance: # and (x, value_row) not in beacons:
                visited.add((x, value_row))
                ans += 1

# print(details)
    
def get_tuning(x, y):
    return x* 4000000 + y

print("ans", ans)
print("ans", len(visited))
# print(visited)
for x in range(0, max_idx + 1):
    print(x)
    for y in range(0, max_idx + 1):
        if (x, y) not in visited:
            print(x, y)
            print('tune', get_tuning(x, y))
# print(visited)
# print(visited)

    



