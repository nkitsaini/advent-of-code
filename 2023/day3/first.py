import sys
from pprint import pprint
from collections import *
import string
from typing import *



T = TypeVar('T')
def dbg(val: T) -> T:
    print('---', val, file=sys.stderr)
    return val


DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
]


def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')

    ans = 0

    # Solve


    
    for idx, line in enumerate(lines):

        digit = ""
        adjacent = False
        for cidx, char in enumerate(line):
            if not char.isdigit():
                if digit != "" and not adjacent:
                    print(digit)
                    ans += int(digit)
                digit = ""
                adjacent = False
                    
            if char.isdigit():
                digit += char
                for dx in [1, 0, -1]:
                    nidx = idx + dx
                    ncidx = cidx + dy
                    if nidx >=0 and ncidx >=0 and nidx < len(lines) and ncidx < len(line) and not lines[nidx][ncidx].isdigit() and lines[nidx][ncidx] != '.':
                        adjacent = True

        if digit != "" and not adjacent:
            print(digit)
            ans += int(digit)

        
        loc_ans = 0
        
        
                
            
        

    


    


    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
