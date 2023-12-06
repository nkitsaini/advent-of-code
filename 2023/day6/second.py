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

def trim_split(value: str, sep: str = " ", remove_empty: bool = True) -> List[str]:
    rv = []
    return [x.strip() for x in value.strip().split(sep) if x.strip() != ""]

def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')

    ans = 0
    array = []

    times = [int(x) for x in trim_split(trim_split(lines[0], ":")[1])]
    distance = [int(x) for x in trim_split(trim_split(lines[1], ":")[1])]
    print(times)
    print(distance)

    for t, d in zip(times, distance):
        t
        ...



    print(array)
    print(ans)
    

    
def repl():
    ...

if __name__ == "__main__":
    # repl()
    main()
