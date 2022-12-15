from typing import *
import re
# import rangetreefrom rangetree import RangeTree
from rangetree import RangeTree
from intervaltree import Interval, IntervalTree

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
max_idx = 3000000
visited = set()
ranges = []

# def add_range(G)
def get_tuning(x, y):
    return x* 4000000 + y

# for (sx, sy), (bx, by) in details:
for value_row in range(0, max_idx + 1)[::-1]:
    if value_row %1000 == 0:
        print(value_row)
    # rt = RangeTree()
    rt = IntervalTree()
    rt[0:max_idx+1] = 0
    for s, b in details:
        distance = dist(s, b)
        initial_dist = abs(s[1] - value_row)

        extra_dist = distance - initial_dist

        max_x = s[0] + extra_dist
        min_x = s[0] - extra_dist

        if max_x < min_x:
            continue

        # rt[min_x:max_x+1] = 1
        rt[min_x:max_x+1] = 1
        # for x in range(min_x, max_x + 1):
        #     if dist(s, (x, value_row)) <= distance: # and (x, value_row) not in beacons:
        #         visited.add((x, value_row))
        #         ans += 1
    x = 0
    while x < max_idx + 1:
    # for x in range(0, max_idx + 1):
        # print(x, y, ranges[x][y])
        # if ranges[y][x] == 0:
        
        if len(rt[x]) == 1:
            print(x, value_row)
            print('tune', get_tuning(x, value_row))
            # print('tune', get_tuning(value_row, x))
            raise Exception()
        else:
            x += 1
            for k in rt[x]:
                if k[2] == 1:
                    x = max(x, k[1])
                # if k[]
        

    # ranges.append(rt)

# print(details)
    

print("ans", ans)
print("ans", len(visited))
# print(visited)
for y in range(0, max_idx + 1):
    print("=======================", y)
    # print(ranges[y])
    # if (x == )
    for x in range(0, max_idx + 1):
        # print(x, y, ranges[x][y])
        # if ranges[y][x] == 0:
        if len(ranges[y][x]) == 1:
            print(x, y)
            print('tune', get_tuning(x, y))
            raise Exception()
        # if (x, y) not in visited:
        #     print(x, y)
        #     print('tune', get_tuning(x, y))

    



