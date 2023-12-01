from typing import *
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

area = [['.' for _ in range(1001)] for _ in range(10001)]
    
min_stopper = 0
ans = 0

while True:
    line = get_line()
    if line is None: break
    rock = [(int(y), int(x)) for x, y in [j.split(',') for j in [k.strip() for k in line.split('->')]]]
    for (point1, point2) in zip(rock, rock[1:]):
        min_stopper = max(min_stopper, point1[0])
        min_stopper = max(min_stopper, point2[0])
        if point1[0] == point2[0]:
            # for y in range(point1[1], point2[1] +1):
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) +1):
                area[point1[0]][y] = '#'
        else:
            for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) +1):
                area[x][point1[1]] = '#'

for i in range(0, 1001):
    area[min_stopper+2][i] = '#'

print(min_stopper)
# at rest or not
def fall() -> bool:
    assert area[0][500] == '.'
    current = (0, 500)
    moves = [(1, 0), (1, -1), (1, 1)]
    while True:
        found = False
        for move in moves:
            cx_new = current[0] + move[0]
            cy_new = current[1] + move[1]
            # print(area[current[0]][current[1]])
            # print(area[cx_new][cy_new])
            # print(cx_new, cy_new, min_stopper, current[0])
            if area[cx_new][cy_new] == '.':
                # print(cx_new, cy_new)
                current = (cx_new, cy_new)
                found = True
                break
        if not found:
            # print(cx_new, cy_new)
            area[current[0]][current[1]] = 'o'
            current = (cx_new, cy_new)
            return True
    # print(current)
    return False
        
def print_area():
    for row in area[:20]:
        print(row[490:510])

# exit()
# while fall() and ans <= 30:
# while area[0][500] == '.' and ans <= 100: # and ans <= 30:
while area[0][500] == '.': # and ans <= 30:
    fall()
    print_area()
    print(ans)

    ans += 1


    
    

print("ans", ans)

    



