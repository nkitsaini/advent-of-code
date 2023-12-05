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

    mappings = defaultdict(lambda: defaultdict(dict))

    for split in splits[1:]:
        sp_lines = split.strip().splitlines()
        if len(sp_lines) == 0:
            continue

        source, target = sp_lines[0].split()[0].split("-to-")
        print("=source, target", source, target)
        for range_query in sp_lines[1:]:
            dest_start, dest_end, count = range_query.split()

   
    for idx, line in enumerate(lines):
        loc_ans = 0
        loc_array = []
        # Solvekkjkj

    


    print(array)
    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
