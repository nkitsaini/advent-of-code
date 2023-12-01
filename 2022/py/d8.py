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
trees = []

while True:
    line = get_line()
    if line is None: break
    trees.append([int(x) for x in line])

pprint(trees)

def is_visible(i, j):
    height = trees[i][j]
    v1 = True
    v2 = True
    v3 = True
    v4 = True
    for a in range(0, i):
        if trees[a][j] >= height:
            v1 = False
    for a in range(i+1, len(trees)):
        if trees[a][j] >= height:
            v2 = False
    for a in range(0, j):
        if trees[i][a] >= height:
            v3 = False
    for a in range(j+1, len(trees[0])):
        if trees[i][a] >= height:
            v4 = False
    return any([v1, v2, v3, v4])

for i in range(len(trees)):
    for j in range(len(trees[0])):
        if is_visible(i, j):
            ans += 1


print("ans", ans)

    



