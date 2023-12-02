import sys
from pprint import pprint
from collections import *
import string
from typing import *



T = TypeVar('T')
def dbg(val: T) -> T:
    print('---', val)
    return val


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
        sets = line.split(':')[1].split(';')
        max_blue = 0
        max_red = 0
        max_green = 0
        for balls in sets:
            for ball in balls.split(','):
                print(ball)
                count, color = ball.strip().split(' ')
                if 'green' == color:
                    max_green = max(max_green, int(count))
                if 'blue' == color:
                    max_blue = max(max_blue, int(count))
                if 'red' == color:
                    max_red = max(max_red, int(count))
        loc_ans = 1
        for val in [max_blue, max_red, max_green]:
            if val == float('inf'):
                val = 0
            loc_ans *= val 
        print(loc_ans, max_blue, max_red, max_green)
        ans += loc_ans

        # if max_blue <= 14 and max_red <= 12 and max_green <= 13:
        #     ans += idx + 1

                
            
        

    


    


    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
