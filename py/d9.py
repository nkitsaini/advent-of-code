from typing import *
from pprint import pprint
from collections import defaultdict
import tempfile

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

    
ans = 0

while True:
    line = get_line()
    if line is None: break

print("ans", ans)

    



