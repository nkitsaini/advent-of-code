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

# CARD_ORDERS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_ORDERS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_card_score(card: str):
    return CARD_ORDERS.index(card)

def get_hand_score(card: str):
    # ...........
    counts = Counter(card)
    card_map = ''.join([chr(ord('a') + get_card_score(x)) for x in card])
    if sorted(counts.values()) == [5]:
        return '0' + card_map
    if sorted(counts.values()) == [1,4]:
        return '1' + card_map
    if sorted(counts.values()) == [2, 3]:
        return '2' + card_map
    if sorted(counts.values()) == [1, 1, 3]:
        return '3' + card_map
    if sorted(counts.values()) == [1, 2, 2]:
        return '4' + card_map
    if sorted(counts.values()) == [1, 1, 1, 2]:
        return '5' + card_map
    if sorted(counts.values()) == [1, 1, 1, 1, 1]:
        return '6' + card_map

def get_hand_score_complex(card: str):
    for idx in range(len(card)):
        if card[idx] == 'J':
            new_card = 
    # if len(set(card)) == 1:
    #     return '6' + card
    # if max(counts.values()) == 4:
    #     return '5' + card
    # if sorted(counts.values()) == [2, 3]:
    #     return '4' + card
    # if sorted(counts.values()) == [1, 1, 3]:
    #     return '3' + card
    # if sorted(counts.values()) == [1, 2, 2]:
    #     return '2' + card
    # if sorted(counts.values()) == [1, 1, 1, 2]:
    #     return '1' + card
    # if sorted(counts.values()) == [1, 1, 1, 1, 1]:
    #     return '0' + card
    raise Exception()

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

    cards = []
    for idx, line in enumerate(lines):
        card, amount = line.split()
        cards.append((get_hand_score(card), card, int(amount)))
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
