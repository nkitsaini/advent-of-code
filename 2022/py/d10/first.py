from typing import *
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

register_val = [1]

def noop():
    last_val = register_val[-1]
    register_val.append(last_val)

def add(amount):
    last_val = register_val[-1]
    # register_val.append(last_val)
    register_val.append(last_val)
    register_val.append(last_val + amount)

while True:
    line = get_line()
    if line is None: break
    if line == "noop":
        noop()
    else:
        amount = int(line.split(' ')[-1])
        add(amount)


# sprite = [1, 1, 1] + ([0]*50)
screen = [['.']*40 for _ in range(6)]
print(register_val[:10])
for i, v in enumerate(register_val):
    current_col = i%40
    current_row = i//40
    print(current_col, v)
    if current_col+1 in [v, v+1, v+2]:
        screen[current_row][current_col] = '#'

for row in screen:
    print(''.join(row))





# for i in [20, 60, 100, 140, 180, 220]:
#     ans += register_val[i-1]*i
#     print(register_val[i-1]*i)

print("ans", ans)

    



