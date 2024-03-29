import sys
import re
from pprint import pprint
from collections import *
import string
from typing import *



T = TypeVar('T')
def dbg(val: T) -> T:
    print('---', val, file=sys.stderr)
    return val

DIRECTION_NAME = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}
DIRECTION_NAME_REVERSED = {v: k for k, v in DIRECTION_NAME.items()}

DIRECTIONS = list(DIRECTION_NAME_REVERSED.keys())
DIRECTIONS_EDGE = [
    *DIRECTIONS,
    (1, -1),
    (-1, 1),
    (-1, -1),
    (1, 1),
]

# Return ranges
def map_range(start, end, ranges):
    rv = []
    ranges.sort(key=lambda x: (x[1], x[2]))
    last = start
    for (dest, src, count) in ranges:
        if src > last:
            rv.append((last, min(end, src + count)))
            last = min(end, src + count)

        starting_point = max(src, last)
        ending_point = min(src + count, end)
        if ending_point <= starting_point or ending_point <= last or starting_point >= end:
            continue
        last += (ending_point - starting_point)
        rv.append((starting_point + dest - src, ending_point + dest - src))
    if last != end:
        rv.append((last, end))
    return [x for x in rv if x[0] != x[1]]

def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')

    ans = 0
    array = []

    seeds = [int(x) for x in splits[0].split(':')[1].strip().split()]
    print(seeds)

    mappings = defaultdict(lambda: defaultdict(list))

    for split in splits[1:]:
        sp_lines = split.strip().splitlines()
        if len(sp_lines) == 0:
            continue

        source, target = sp_lines[0].split()[0].split("-to-")
        print("=source, target", source, target)
        for range_query in sp_lines[1:]:
            dest_start, src_start, count = range_query.split()
            # mappings[source][target].append((dest_start, src_start, count))
            mappings[target][source].append((int(dest_start), int(src_start), int(count)))


    path = ["seed", 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    # path = ["seed", 'soil']

    print(mappings)
    values = seeds
    value_ranges = []
    for value, rng in zip(seeds[::2], seeds[1::2]):
        value_ranges.append((value, value+rng))
    values = value_ranges





        

    def min_range(ranges):
        return min([r[0] for r in ranges])



    past = "seed"
    for p in path[1:]:
        # print(values)
        # maps = mappings[past][p]
        maps = mappings[p][past]
        # print(maps, past, p)
        print("=== values", values, p)
        next_values = []
        print("values", len(values), len(maps))
        # for value in values:
        #     found = False
        for start, rng in values:
            next_values.extend(map_range(start, rng, maps))
            # for dest, src, count in maps:
            #     dest, src, count = int(dest), int(src), int(count)
            #     # print(value, dest, src, count)
            #     if src + count > value and src <= value:
            #         # value = 13, src = 10, dest = 90, count = 7
            #         next_values.append(dest + value - src)
            #         # print("Found value")
            #         found = True
            #         break
            # if not found:
            #     next_values.append(value)
        values = list(set(next_values))
        past = p
    print(values)
    print(min(values))
    print(min_range(values))
                
    #     ...

   
    # for idx, line in enumerate(lines):
    #     loc_ans = 0
    #     loc_array = []
    #     # Solvekkjkj

    


    # print(array)
    # print(ans)
                 


    
    

if __name__ == "__main__":
    # print(map_range(100, 50, [(11, 100, 3), (15, 110, 20), (0, 90, 3)]))
    main()
