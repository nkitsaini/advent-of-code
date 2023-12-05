import sys
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

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]
DIRECTIONS_EDGE = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
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

    # Solve


    
    for idx, line in enumerate(lines):
        loc_ans = 0
        loc_array = []

        



    print(array)
    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
