from typing import *
import sys
sys.setrecursionlimit(1000000)
import functools
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

# @functools.wraps(print)
# def debug(*args, **kwargs):
#     return
#     print(*args, **kwargs)

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

ans = 0
cubes = []
cube_set = set()

for line_no in range(100000000):
    line = get_line()
    if line == None: break
    cubes.append(tuple(map(int, line.split(','))))

cube_set = set(cubes)
      
for i, (x, y, z) in enumerate(cubes):
    cube = [x, y, z]
    for side in [0, 1, 2]:
        cube[side] += 1
        if tuple(cube) not in cubes:
            ans += 1
        cube[side] -= 2
        if tuple(cube) not in cubes:
            ans += 1
        cube[side] += 1

    # for j, (nx, ny, nz) in enumerate(cubes):
    #     if i == j:
    #         continue
    #     for side in [0, 1, 2]:
    #         if 

directions = [
    (0, 0, -1),
    (0, 0, +1),
    (0, -1, 0),
    (0, +1, 0),
    (-1, 0, 0),
    (+1, 0, 0),
]
visited = set()

limit = (0, 22)
# limit = (1, 9)
for ci in range(*limit):
    for cj in range(*limit):
        for ck in range(*limit):
            
            cube = (ci, cj, ck)
            if cube in visited:
                continue
            if cube in cube_set:
                continue
            current_visited = set([cube])
            total_surface = [0]
            debug_mode = cube == (2, 2, 5)
            debug_mode = False
            def debug(*args, **kwargs):
                if debug_mode:
                    print(*args, **kwargs)
            debug("=====================================================")
            debug("=====================================================")
            debug("=====================================================")
            debug("=====================================================")
            debug("=====================================================")
            def dfs(cube) -> bool: # returns true if should substract
                debug("dfs", cube)
                is_open = False
                for dx, dy, dz in directions:
                    nx = cube[0] + dx
                    ny = cube[1] + dy
                    nz = cube[2] + dz
                    new_cube = (nx, ny, nz)
                    if new_cube in current_visited:
                        continue
                    is_out_of_bound = False
                    for val in [nx, ny, nz]:
                        if val < limit[0] or val >= limit[1]:
                            is_out_of_bound = True
                            debug("is_open", (new_cube))
                            is_open |= True
                    debug(is_out_of_bound)
                    if is_out_of_bound: continue
                    debug("nc", new_cube)
                    if new_cube in cubes:
                        debug("Adding surf", new_cube)
                        total_surface[0] += 1
                        continue
                    if new_cube not in current_visited:
                        current_visited.add(new_cube)
                        dfs(new_cube)
                debug("is_open", is_open)
                return not is_open
            debug(visited, current_visited, total_surface)
            if dfs(cube):
                debug("It is subtracting", cube, total_surface)
                ans -= total_surface[0]
            # if cube == (2, 2, 5):
            debug(visited, current_visited, total_surface)
            # if (2, 2, 5) in current_visited:
            #     raise Exception(cube)
            visited = visited.union(current_visited)
            debug("====================")


# directions.remove((0, 0, 0))
# for gap_height in range(1, len(cubes)):
#     for gap_width in range(1, len(cubes)//(gap_height+1)):
#         for gap_length in range(1, len(cubes)// ((gap_height + 1) * (gap_width+1))):

#             def is_internal(cube) -> bool:
#                 for i in range(gap_height):
#                 ...
#             for cube in cubes:
#                 if is_internal(cube):
#                     ans -= gap_height * gap_length * gap_width # Might be wrong
#             # print(gap_width, gap_height, gap_length)
    
print(cubes)
print(ans)


print(min(x[0] for x in cubes))
print(max(x[0] for x in cubes))
print(min(x[1] for x in cubes))
print(max(x[1] for x in cubes))
print(min(x[2] for x in cubes))
print(max(x[2] for x in cubes))