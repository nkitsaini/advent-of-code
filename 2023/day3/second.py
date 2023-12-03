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


    
    # for idx, line in enumerate(lines):
    #     pass
        
        
                
            
        

    


    


    print(ans)
                 


    
    

if __name__ == "__main__":
    main()
