from typing import *
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

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

valves = {}
# total_runs = 0
# for i in range(0, 16):
#     my_opens = i
#     elp_opens = 15 - i
#     ...

ans = 0

i = 0
while True:
    line = get_line()
    if line is None: break
    print('line', line)
    match = re.match(r"Valve (\w\w) .*=(\d+).*valves? (.*)", line)

    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    valves[match.group(1)] = [int(match.group(2)), match.group(3).replace(' ', '').split(','), i]

    i += 1

print(valves)

vlv = deepcopy(valves)
opened_valves = set()

# open_bits = 0
cache = {}

@lru_cache(100000000)
def get_max_pressure(remaining_time: int = 30, valve: str = 'AA', open_bits: int = 0):
    # print(remaining_time, valve, open_bits)
    if remaining_time == 0:
        return 0
    max_pressure = 0
    if 1<<vlv[valve][2] & open_bits == 0 and vlv[valve][0] != 0:
        new_pressure = (remaining_time - 1) *  vlv[valve][0]
        open_bits += 1<<vlv[valve][2]
        max_pressure = max(max_pressure, new_pressure + get_max_pressure(remaining_time-1, valve, open_bits))
        open_bits -= 1<<vlv[valve][2]

    for next_valve in vlv[valve][1]:
        max_pressure = max(max_pressure, get_max_pressure(remaining_time-1, next_valve, open_bits))

    return max_pressure


print(get_max_pressure())
print("ans", ans)

    



