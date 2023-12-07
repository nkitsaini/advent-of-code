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

CARD_ORDERS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def get_card_score(card: str):
    return CARD_ORDERS.index(card)

def compare_cards(card1: str, card2: str):
    return 

def trim_split(value: str, sep: str = " ", remove_empty: bool = True) -> List[str]:
    rv = []
    return [x.strip() for x in value.strip().split(sep) if x.strip() != ""]

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

    for idx, line in enumerate(lines):
        ...


    print(array)
    print(ans)
    

    
def repl():
    ...

if __name__ == "__main__":
    # repl()
    main()
