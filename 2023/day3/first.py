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

    GEAR_VALUES = defaultdict(list)

    
    for idx, line in enumerate(lines):
        gear_idx = []
        digit = ""
        adjacent = False
        for cidx, char in enumerate(line):
            if not char.isdigit():
                if digit != "" and adjacent:
                    print(digit)
                    # ans += int(digit)
                    for gear_i in set(gear_idx):
                        GEAR_VALUES[gear_i].append(int(digit))
                digit = ""
                gear_idx = []
                adjacent = False
                    
            if char.isdigit():
                digit += char
                for dx in [1, 0, -1]:
                    for dy in [1, 0, -1]:
                        nidx = idx + dx
                        ncidx = cidx + dy
                        if nidx >=0 and ncidx >=0 and nidx < len(lines) and ncidx < len(line) and not lines[nidx][ncidx].isdigit() and lines[nidx][ncidx] == '*':
                            gear_idx.append((nidx, ncidx))
                            adjacent = True

        if digit != "" and adjacent:
            print(digit)
            # ans += int(digit)
            for gear_i in set(gear_idx):
                GEAR_VALUES[gear_i].append(int(digit))
            gear_idx = []


        
        loc_ans = 0
        
        
                
            
        

    

    sets = set()
    # wrong = 13121332
    for k, val in GEAR_VALUES.items():
        if len(val) != 2:
            continue
        print(k, val)
        if tuple(val) in sets:
            continue
        sets.add(tuple(val))

        ans += val[0] * val[1]
    


    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
