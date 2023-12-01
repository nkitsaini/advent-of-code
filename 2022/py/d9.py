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
tail = [0, 0]
visited = set([tuple(tail)])
head = [0, 0]

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def move_head(d):

    dx, dy = directions[d]
    head[0] += dx
    head[1] += dy

def move_tail():
    if head == tail:
        return
    if abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1:
        return

    if head[0] == tail[0] and abs(head[1] - tail[1]) > 1:
        tail[1] = (head[1] + tail[1])//2
        return tail
    if head[1] == tail[1] and abs(head[0] - tail[0]) > 1:
        tail[0] = (head[0] + tail[0])//2
        return tail
    
    
    if head[0] > tail[0]:
        tail[0] += 1
    elif head[0] < tail[0]:
        tail[0] -= 1

    if head[1] > tail[1]:
        tail[1] += 1
    elif head[1] < tail[1]:
        tail[1] -= 1
    return tail
    
while True:
    line = get_line()
    if line is None: break

    d, count = line.split()
    count = int(count)
    for i in range(count):
        move_head(d)
        move_tail()
        visited.add(tuple(tail))


print("ans", len(visited))
# print(visited)
print("ans", ans)

    



