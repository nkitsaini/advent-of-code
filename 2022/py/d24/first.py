from typing import *
import re
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

ans = 0

values = []

start = (0, 1)
end = None
while True:
    line = get_line()
    if line is None: break
    values.append(list(line))


def move_one_step(values) -> List[List[str]]:
    rv = []
    for 
end = (len(values) - 1, len(values[0]) - 2)
print(start, end)
pprint(values)
print("ans", ans)