import sys
import itertools
import re
from pprint import pprint
# from sympy.solvers import solve
# from sympy import Symbol
from collections import *
import string
from typing import *


# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def lcm_all(*args: int):
    arg = list(args)
    while len(arg) > 1:
        last = arg.pop()
        last2 = arg.pop()
        arg.append(compute_lcm(last, last2))
    return arg[0]
        


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

    instructions = lines[0].strip()
    graph = defaultdict()

    
    for idx, line in enumerate(lines[2:]):
        src, nexts = trim_split(line, "=")
        left, right = trim_split(nexts.strip("(").strip(")"), ",")
        graph[src] = {"left": left, "right": right}

    values = [k for k in graph.keys() if k.endswith("A")]
    steps_until_z: DefaultDict[str, List[int]] = defaultdict(list)

    def rep(values):
        while True:
            for val in values:
                yield val
        
    
    for value in values:
        print("--- value", value)
        current = value
        founds = set([value])
        for idx, instruct in enumerate(rep(instructions)):
            if instruct == "L":
                current = graph[current]['left']
            elif instruct == "R":
                current = graph[current]['right']
            else:
                print(instruct)
                raise Exception()
            # print(current)
            if current[2] == 'Z':
                steps_until_z[value].append(idx)

            if ((idx + 1) % len(instructions) == 0):
                if current in founds:
                    break
                else:
                    founds.add(current)

    print(steps_until_z.values())
    return


    

    def is_found():
        for val in values:
            if val[2] != "Z":
                return False
        return True

    i = 0
    found = False
    while not found:
        for instruct in instructions:
            i += 1
            if is_found():
                found = True
                break
            next_values = []
            for current in values:
                if instruct == "L":
                    current = graph[current]['left']
                elif instruct == "R":
                    current = graph[current]['right']
                else:
                    raise Exception()
                next_values.append(current)
            values = next_values
        if is_found():
            found = True
            break
            


        

    print(array)
    print(i)
    

    
def repl():
    ...

if __name__ == "__main__":
    # repl()
    main()
