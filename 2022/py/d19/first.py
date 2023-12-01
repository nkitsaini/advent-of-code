from typing import *
import sys
sys.setrecursionlimit(1000000)
import functools
import itertools
from functools import lru_cache
from copy import deepcopy
import re
from functools import cmp_to_key
import math
import intervaltree
from dataclasses import dataclass
from pprint import pprint
from collections import defaultdict
import tempfile

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

def dist(p1, p2) -> int:
    return abs(p1[0] -p2[0]) + abs(p1[1] - p2[1])

# @functools.wraps(print)
# def debug(*args, **kwargs):
#     return
#     print(*args, **kwargs)

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}
directions3d = [
    (0, 0, -1),
    (0, 0, +1),
    (0, -1, 0),
    (0, +1, 0),
    (-1, 0, 0),
    (+1, 0, 0),
]

ans = 0
for line_no in range(100000000):
    line = get_line()
    if line == None: break

print(ans)
