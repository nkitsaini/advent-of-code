import sys
from pprint import pprint
from collections import *
from typing import *


T = TypeVar('T')
def dbg(val: T) -> T:
    print('---', val)
    return val


values = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
names = list(values.keys())

def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')


    ans = 0
    for line in lines:
        val = ""

        isEnd = False
        for idx, char in enumerate(line):

            for name in names:
                if line[idx:].startswith(name):
                    val += str(values[name])
                    isEnd = True
                    print("========", val)
                    break
            if isEnd:
                break

            if char.isdigit():
                val = char
                break

        isEnd = False
        for idx, char in enumerate(reversed(line)):
            for name in names:
                if "".join(reversed(line))[idx:].startswith("".join(reversed(name))):
                    val += str(values[name])
                    isEnd = True
                    print("========", val)
                    break
            if isEnd:
                break
            if char.isdigit():
                val += char
                break
        ans += int(val)
        print(val)
    print(ans)

                


    
    

if __name__ == "__main__":
    main()
