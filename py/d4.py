from typing import *
def get_line() -> 'str | None':
    try:
        return input().strip()
    except EOFError:
        return None


def get_range(work) -> Tuple[int, int]:
    return tuple([int(x) for x in work.split('-')])

def contains(x, y):
    (x1, y1) = x
    (x2, y2) = y
    if (x2 <= x1 and y2 >= y1):
        return True
    return False

ans = 0
while True:
    line = get_line()
    if line is None: break
    [e1, e2] = line.split(',')
    r1 = get_range(e1)
    r2 = get_range(e2)
    print(r1, r2)
    if contains(r1, r2) or contains(r2, r1):
        ans += 1



print(ans)