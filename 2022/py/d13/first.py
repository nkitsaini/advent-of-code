from typing import *
from functools import cmp_to_key
import math
from dataclasses import dataclass
from pprint import pprint
from collections import defaultdict
import tempfile

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def compare(p1, p2, i = 0) -> Optional[bool]:

    if i >= len(p1) and i < len(p2):
        return True
    if i < len(p1) and i >= len(p2):
        return False
    if i == len(p1) and i == len(p2):
        return None

    if isinstance(p1[i], int) and isinstance(p2[i], int):
        if p1[i] < p2[i]:
            return True
        if p1[i] > p2[i]:
            return False
        return compare(p1, p2, i+1)
    
    if isinstance(p1[i], list) and isinstance(p2[i], list):
        res = compare(p1[i], p2[i])
        if res != None:
            return res
        return compare(p1, p2, i+1)

    v1 = [p1[i]] if isinstance(p1[i], int) else p1[i]
    v2 = [p2[i]] if isinstance(p2[i], int) else p2[i]
    
    res = compare(v1, v2)
    if res != None:
        return res
    return compare(p1, p2, i+1)

    

    
ans = 0
i = 0
packets = []
while True:
    i += 1

    p1 = get_line()
    if p1 is None: break
    p2 = get_line()
    p1 = eval(p1)
    p2 = eval(p2)
    packets.append(p1)
    packets.append(p2)
    # if (compare(p1, p2)):
    #     ans += i
    

    if get_line() is None: break
packets.append([[2]])
packets.append([[6]])
def my_key(packet1, packet2):
    return -1 if compare(packet1, packet2) else 1
packets.sort(key=cmp_to_key(my_key))

i1 = packets.index([[2]]) + 1
i2 = packets.index([[6]]) + 1
print("ans", i1*i2)

    



