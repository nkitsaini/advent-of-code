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

    print(mappings)
    values = seeds
    value_ranges = []
    for value, rng in zip(seeds[::2], seeds[1::2]):
        value_ranges.append((value, rng))

    # Return ranges
    def map_range(start, rng, ranges):
        rv = []
        ranges.sort(key=lambda x: (x[1], x[2]))
        last = start
        end = start + rng
        for (dest, src, count) in ranges:
            if last < src:
                rv.append((last, src-last))
                last = src
                continue
            if end > src + count:
                rv.append((src, src+count))
                last = last+count
                continue
            rv.append((src, src + end-last))
            last = end
        return rv

                


        

    def min_range(ranges):
        return min([r[0] for r in ranges])



    past = "seed"
    for p in path[1:]:
        # print(values)
        # maps = mappings[past][p]
        maps = mappings[p][past]
        # print(maps, past, p)
        next_values = []
        for value in values:
            found = False
            for start, rng in values:
                next_values.extend(map_range(values, maps))
            # for dest, src, count in maps:
            #     dest, src, count = int(dest), int(src), int(count)
            #     # print(value, dest, src, count)
            #     if src + count > value and src <= value:
            #         # value = 13, src = 10, dest = 90, count = 7
            #         next_values.append(dest + value - src)
            #         # print("Found value")
            #         found = True
            #         break
            if not found:
                next_values.append(value)
        values = next_values
        past = p
    print(values)
    print(min(values))
                
    #     ...

   
    # for idx, line in enumerate(lines):
    #     loc_ans = 0
    #     loc_array = []
    #     # Solvekkjkj

    


    # print(array)
    # print(ans)
                 


    
    

if __name__ == "__main__":
    main()
