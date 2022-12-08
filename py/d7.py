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

fs_rec = lambda: defaultdict(fs_rec)
file_system = fs_rec()

curr_pointer = file_system
parents = []
def down(val: str):
    global curr_pointer
    parents.append(curr_pointer)
    curr_pointer = curr_pointer[val]

def up():
    global curr_pointer
    curr_pointer = parents.pop()

get_line()
while True:
    line = get_line()
    if line is None: break

    if line.startswith('$ cd'):
        if 'cd ..' in line:
            up()
        else:
            val = line.split(' ')[-1]
            down(val)

    if line.startswith('$ ls'):
        while True:
            curr = get_line()
            if curr == None: break
            if curr.startswith('dir'):
                continue
            if curr == 'end':
                break
            print(curr)
            size, name = curr.split(' ')
            curr_pointer[name] = size

pprint(file_system)

to_process = [file_system]

def get_rec_size(d):
    ans1 = 0
    for name, child in d.items():
        print(name, child)
        if isinstance(child, dict):
            ans1 += get_rec_size(child)
        else:
            ans1 += int(child)
    return ans1

extra_space = 70000000 - get_rec_size(file_system)
space_req = 30000000 - extra_space

ans = float('inf')
while to_process:
    new_to_process = []
    for d in to_process:
        val = get_rec_size(d)
        if val >= space_req:
            ans = min(ans, val)
        for name, child in d.items():
            if isinstance(child, dict):
                print(name)
                new_to_process.append(child)
    to_process = new_to_process


print("ans", ans)

    



