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

def score(i, j):
    height = trees[i][j]
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0

    mv1 = height
    mv2 = height
    mv3 = height
    mv4 = height

    for a in range(0, i)[::-1]:
        if trees[a][j] >= height:
            v1 += 1
            break
        v1 += 1
    for a in range(i+1, len(trees)):
        if trees[a][j] >= height:
            v2 += 1
            break
        v2 += 1
    for a in range(0, j)[::-1]:
        if trees[i][a] >= height:
            v3 += 1
            break
        v3 += 1
    for a in range(j+1, len(trees[0])):
        if trees[i][a] >= height:
            v4 += 1
            break
        v4 += 1
    print(v1, v2, v3, v4, i, j)
    return v1*v2*v3*v4

for i in range(len(trees)):
    for j in range(len(trees[0])):
        ans = max(ans, score(i, j))

print("ans", ans)

    



