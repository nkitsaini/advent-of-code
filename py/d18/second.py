from typing import *
import itertools
from functools import lru_cache
from copy import deepcopy
import re
from functools import cmp_to_key
import math
import intervaltree
from dataclasses import dataclass
from pprint import pprint
from collections import defaultdict
import tempfile

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

def dist(p1, p2) -> int:
    return abs(p1[0] -p2[0]) + abs(p1[1] - p2[1])

def debug(*args, **kwargs):
    return
    print(*args, **kwargs)
directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

ans = 0
wind = get_line()
print(wind)

area = [['.' for _ in range(7)] for _ in range(2022*4)]
area = [['.' for _ in range(2022*10)] for _ in range(7)]
"""
1.
####

2.
.#.
###
.#.

3.
..#
..#
###

4.
#
#
#
#

5.
##
##
"""

def __get_rock_shape(i):
    if i == 0:
        return [(i, 0) for i in range(4)]
    elif i == 1:
        return [(0, 0), (0, -1), (0, -2), (-1, -1), (1, -1)]
    elif i == 2:
        return [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)]
    elif i == 3:
        return [(0, -i) for i in range(4)]
    elif i == 4:
        return [(0, 0), (0, 1), (-1, 1), (-1, 0)]
    raise Exception(i)

def reverse_shape(shape):
    # return shape
    return [(x, -1*y) for x, y in shape]

def get_rock_shape(i):
    return reverse_shape(__get_rock_shape(i))

wind_i = 0
max_height = 0
# max_height = -1
# for i in range(1000000000000):
cache = defaultdict(list)
# for i in range(2022):

repeat_val = {21, 20, 22, 19}
repeat_val = {21, 20, 22, 19, 23, 24, 25, 26, 27, 28, 29, 18, 17}
repeat_val = {307, 308, 309}
repeat_val = {1589, 1297}
repeats = dict()
to_find = None
found_at = None
found_at_key = None
for i in range(1000000000):
# for i in range(5):
    rock_no = i%5
    rock_shape = get_rock_shape(rock_no)
    left = min(rock_shape, key=lambda x: x[0])
    bottom = min(rock_shape, key=lambda x: x[1])
    debug(left, bottom)

    start_y = max_height + 3
    start_x = 2
    x_offset =  start_x - left[0]
    y_offset =  start_y - bottom[1]
    # y_offset = left[1] - start_y
    left[0]
    debug(x_offset, y_offset)
    debug([(x+x_offset, y+y_offset) for x, y in rock_shape])
    # exit()

    def in_check():
        for (x, y) in rock_shape:
            x += x_offset
            y += y_offset
            if not (0 <= x <= 6):
                return False
            if not (0 <= y):
                return False
            if area[x][y] != '.':
                return False
        return True
    
    def fill_area(char='#'):
        global max_height
        for (x, y) in rock_shape:

            x += x_offset
            y += y_offset
            if char == '#':
                debug('fill', x, y)
                max_height = max(max_height, y+1)
            area[x][y] = char
    
    def print_area():
        return
        for i in range(20)[::-1]:
            for j in range(7):
                print(area[j][i], end='')
            print()
        print('---------------')
    
    def dbg_print():
        return
        fill_area('@')
        print_area()
        fill_area('.')

    assert in_check()
    debug(max_height, (x_offset, y_offset))
    debug('starting:')
    dbg_print()
    def last_n(n=30):
        ans = ''
        for height in range(max_height-n, max_height +1):
            ans += ''.join(area[x][height] for x in range(7))
        return ans
    def print_last_n(n=30):
        ans = ''
        print(max_height, max_height-n, max_height +1)
        for height in range(max_height-n, max_height +1)[::-1]:
            print('doing', height)
            ans += ''.join(area[x][height] for x in range(7)) + '\n'
        print(ans)
        return ans

    key = (wind_i, rock_no, last_n())
    if key in cache:
        # if to_find != None and to_find == (wind_i, rock_no, last_n()):
        #     # print_last_n()
        #     print("=== CACHE", wind_i, i)
        #     print(cache[key], (max_height, i))
        #     exit()
        # elif to_find == None:
        #     second_ans = (max_height, i)
        #     to_find = (wind_i, rock_no, last_n())
        if found_at == None:
            found_at = i
            found_at_key = key
        if len(cache[key]) >= 3:
            print(cache[key])
            pprint(repeats)
            exit()
        else:
            cache[key].append((max_height, i))
    else:
        cache[key].append((max_height, i))
    if found_at and i - found_at in repeat_val:
        repeats[(i, found_at, i-found_at)] = max_height
        new_adds = None
        # for (_f, _f2, _f3) in cache.keys():
        #     if _f == found_at:
        for (_m, _i) in cache[found_at_key]:
            if _i == found_at:
                new_adds = max_height - _m

        repeats[f"i={i} relates to index={found_at} at difference of={i-found_at}):: New Adds= {new_adds}"] = max_height

        
    # for direction in itertools.cycle(list(wind)):
    while True:
        wind_i%=len(wind)
        direction = wind[wind_i]
        wind_i += 1
        x_offset += 1 if direction == '>' else -1
        debug('pushing to', direction)
        if not in_check():
            debug('cant push to ', direction)
            x_offset -= 1 if direction == '>' else -1
        
        dbg_print()

        y_offset -= 1
        debug('moving down')
        if not in_check():
            debug('cant move down')
            y_offset += 1
            fill_area()
            break
        dbg_print()
        pass
        # Move in direction
        # Move down (if can't move down, exit)
    
    print_area()
    # pprint([''.join(x[:20]) for x in area])
        
# for i in range(2022):
#     if all(area[x][i] == '#' for x in range(7)):
#         print("DOOOONE", i)

for i in range(2022)[::-1]:
    print(i+1, end='')
    for j in range(7):
        print(area[j][i], end='')
    print()
    

print(max_height)
print("ans", ans)
