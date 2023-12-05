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


    my_cards = Counter() # Equal to {key: 0}
    
    for idx, line in enumerate(lines):
        loc_ans = 0
        loc_array = []

        cards = line.split(":")[1]
        split1, split2 = cards.split("|")
        winning_cards = []
        me_cards = []
        for card in split1.split():
            if card.strip() != "":
                winning_cards.append(int(card.strip()))
        for card in split2.split():
            if card.strip() != "":
                me_cards.append(int(card.strip()))
        for card in me_cards:
            if card in winning_cards:
                # my_cards[card] += 1
                loc_ans += 1

        # print(my_cards)
        # for card in my_cards.keys():
        #     if card in winning_cards:
        #         # my_cards[card] += 1
        #         loc_ans += my_cards[card]

        for i in range(loc_ans):
            print(idx, i+1+idx+1)
            my_cards[i+1+idx+1] += 1 *(1 +  my_cards[idx+1])
                
            # ans += 2**(loc_ans - 1)

        

    # print(my_cards)
    for card, val in my_cards.items():
        # ans += card * val
        ans +=  val


    print(array)
    print(ans + len(lines))
    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
