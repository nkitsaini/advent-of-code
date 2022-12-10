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
# tail = [0, 0]
tails = [[0, 0] for _ in range(9)]
visited = set([(0, 0)])
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

def move_tail(i):
    tail = tails[i]
    if i == 0:
        head1 = head
    else:
        head1 = tails[i-1]
    if head1 == tail:
        return
    if abs(head1[1] - tail[1]) <= 1 and abs(head1[0] - tail[0]) <= 1:
        return

    if head1[0] == tail[0] and abs(head1[1] - tail[1]) > 1:
        tail[1] = (head1[1] + tail[1])//2
        return tail
    if head1[1] == tail[1] and abs(head1[0] - tail[0]) > 1:
        tail[0] = (head1[0] + tail[0])//2
        return tail
    
    
    if head1[0] > tail[0]:
        tail[0] += 1
    elif head1[0] < tail[0]:
        tail[0] -= 1

    if head1[1] > tail[1]:
        tail[1] += 1
    elif head1[1] < tail[1]:
        tail[1] -= 1
    return tail
    
while True:
    line = get_line()
    if line is None: break

    d, count = line.split()
    count = int(count)
    for i in range(count):
        move_head(d)
        for i in range(len(tails)):
            move_tail(i)
        visited.add(tuple(tails[-1]))
        print(tails, head)


print("ans", len(visited))
# print(visited)
print("ans", ans)
