from typing import *
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
graph = [ ]

start = None
end = None
while True:
    line = get_line()
    if line is None: break
    graph.append(list(line.replace('S', 'a')))
    try:
        j = line.index('E')
        i = len(graph) - 1
        end = (i, j)
    except:
        pass

print(graph, start, end)


def find_min(start) -> int:
    visited = set()
    to_visit = [start]
    steps = 0
    done = False
    while to_visit and not done:
        steps += 1
        new_to_visit = []
        for (i, j) in to_visit:
            for dx, dy in directions.values():
                ni = i + dx
                nj = j + dy
                # print(ni, nj)
                if (ni <0 or ni >= len(graph)):
                    # print('x out range')
                    continue
                if (nj <0 or nj >= len(graph[0])):
                    # print('y out range')
                    continue
                if graph[i][j] not in 'S' and ord(graph[ni][nj] if graph[ni][nj] not in 'SE' else 'z') > ord(graph[i][j]) + 1:
                    # print('greater', ord(graph[ni][nj]), ord(graph[i][j]))
                    continue
                if (ni, nj) in visited:
                    # print('visited')
                    continue
                # if (ni, nj) == (3, 6):
                if (ni, nj) == end:
                    # print("Found from", i, j)
                    done = True
                    break
                new_to_visit.append((ni, nj))
                visited.add((ni, nj))
        # print(new_to_visit)
        to_visit = new_to_visit
    if not done:
        return float('inf')
    return steps

ans = float('inf')
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if (graph[i][j] == 'a'):
            steps = find_min((i, j))
            if (steps == 1):
                print(i, j)
            ans = min(ans, steps)

print("ans", ans)

    



