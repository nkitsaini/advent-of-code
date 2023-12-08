import sys
import re
from pprint import pprint
# from sympy.solvers import solve
# from sympy import Symbol
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
    return [x.strip() for x in value.strip().split(sep) if not remove_empty or x.strip() != ""]

def split_int(value: str, sep: str = " ") -> List[int]:
    rv = []
    return [int(x.strip()) for x in value.strip().split(sep) if x.strip() != ""]

# def solve_quadratics(a, b, c) -> Tuple[float, float]:
#     x = Symbol('x')
#     return tuple(solve(a*x*x + b*x, +c, 0))

def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')

    ans = 0
    array = []

    cards = []
    for idx, line in enumerate(lines):
        card, amount = line.split()
        print("============ card", card)
        cards.append((get_hand_score_complex(card), card, int(amount)))
        print("============ cardscore", cards[-1][0])
    cards.sort(reverse=True)
    print(cards)
    for idx, (hand, card, amount) in enumerate(cards):
        ans += (idx +1) * amount


    # print(array)
    print(ans)
    

    
def repl():
    ...

if __name__ == "__main__":
    # repl()
    main()
