from typing import *
from functools import lru_cache
from copy import deepcopy
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

def dist(p1, p2) -> int:
    return abs(p1[0] -p2[0]) + abs(p1[1] - p2[1])

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

valves = {}

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
    line
print(valves)

vlv = deepcopy(valves)
opened_valves = set()

# open_bits = 0
cache = {}
all_valves_open = 0
for vavls in valves.values():
    if vavls[0] != 0:
        all_valves_open += 1<<vavls[2]

for _, v, _ in valves.values():
    v.sort(key=lambda x: valves[x][0])
# print("total", sum([1 for x in valves.values() if x[0] > 0]))
# exit()
total_valve_score = sum(v[0] for v in valves.values())

@lru_cache(10000000000)
def get_max_pressure(remaining_time: int = 26, my_valve: str = 'AA', elephant_valve: str = 'AA', open_bits: int = 0, my_visits: int = 0, elm_visits = 0):
    global total_valve_score
    assert open_bits <= all_valves_open
    if open_bits == all_valves_open:
        return 0

    if remaining_time == 0:
        return 0

    max_pressure = 0

    for my_option in [0, *vlv[my_valve][1]]:
        for elephent_option in [0, *vlv[elephant_valve][1]]:
            # if (total_valve_score * (remaining_time -1) <= max_pressure):
            #     # print('yes')
            #     break
            #     continue
            if my_option == 0 and not (1<<vlv[my_valve][2] & open_bits == 0 and vlv[my_valve][0] != 0):
                continue
            if elephent_option == 0 and not (1<<vlv[elephant_valve][2] & open_bits == 0 and vlv[elephant_valve][0] != 0):
                continue
            if my_option == 0 and elephent_option==0 and my_valve == elephant_valve:
                continue
            if my_option == elephent_option and my_option != 0:
                continue
            

            def do(option, valve, open_bits) -> Tuple[str, int]:
                global total_valve_score
                if option == 0:
                    new_pressure = (remaining_time - 1) *  vlv[valve][0]
                    open_bits += 1<<vlv[valve][2]
                    total_valve_score -= vlv[valve][0]
                    return valve, open_bits, new_pressure
                else:
                    return option, open_bits, 0


            def revert(option, valve, open_bits) -> open_bits:
                global total_valve_score
                if option == 0:
                    total_valve_score += vlv[valve][0]
                    open_bits -= 1<<vlv[valve][2]
                return open_bits

            nv, no, np =do(my_option, my_valve, open_bits)
            nv2, no2, np2 = do(elephent_option, elephant_valve, no)
            if my_option == 0:
                my_n_v = 0
            else:
                my_n_v = my_visits | (1<<valves[my_valve][2])
            if elephent_option == 0:
                el_n_v = 0
            else:
                el_n_v = elm_visits | (1<<valves[elephant_valve][2])
            # print(nv, nv2)
            [nv, nv2] = sorted([nv, nv2])
            max_pressure = max(max_pressure, np+np2+get_max_pressure(remaining_time-1, nv, nv2, no2, my_n_v, el_n_v))
            ob = revert(my_option, my_valve, no2)
            open_bits = revert(elephent_option, elephant_valve, ob)

    return max_pressure

    # if el_turn:
    #     valve = elephant_valve
    #     rmt = remaining_time 
    #     ov = my_valve
    # else:
    #     valve = my_valve
    #     rmt = remaining_time -1
    #     ov = elephant_valve
 

    # if 1<<vlv[valve][2] & open_bits == 0 and vlv[valve][0] != 0:
    #     new_pressure = (remaining_time - 1) *  vlv[valve][0]
    #     open_bits += 1<<vlv[valve][2]
    #     max_pressure = max(max_pressure, new_pressure + get_max_pressure(rmt, not el_turn, valve, open_bits))
    #     open_bits -= 1<<vlv[valve][2]

    # for next_valve in vlv[valve][1]:
    #     max_pressure = max(max_pressure, get_max_pressure(rmt, not el_turn, next_valve, open_bits))

    # return max_pressure


print(get_max_pressure())
print("ans", ans)

    



