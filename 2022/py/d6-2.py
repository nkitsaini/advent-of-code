from typing import *

def get_line() -> 'str | None':
    try:
        return input().strip("\n")
    except EOFError:
        return None

is_sample = None


sample_stack_height = 3
sample_stacks = 3

real_stack_height = 8
real_stacks = 9

stack_height = None
stacks = None

def get_stacks(line: str) -> List[str]:
    rv = []
    while line:
        val = line[:4].strip('[] ')
        line = line[4:]
        rv.append(val)
    return rv

def update_sample(is_sample):
    global stack_height
    global stacks
    if is_sample:
        stack_height = sample_stack_height
        stacks = sample_stacks
    else:
        stack_height = real_stack_height
        stacks = real_stacks
    
ans = 0

line = get_line()
if is_sample is None:
    is_sample = '[D]' in line
update_sample(is_sample)

stack_vals = [[] for i in range(stacks)]   
st = get_stacks(line)
print(st)
for i, char in enumerate(st):
    if char != '':
        stack_vals[i].append(char)

for i in range(stack_height-1):
    line = get_line()
    st = get_stacks(line)
    print(st)
    for i, char in enumerate(st):
        if char != '':
            stack_vals[i].append(char)

stack_vals = [x[::-1] for x in stack_vals]

def parse_line(line):
    line = line.replace('from', '')
    line = line.replace('move', '')
    line = line.replace('to', '')
    x = [c for c in line.split(' ') if c != '']
    print(x)
    return [int(j) for j in x]
get_line()
get_line()
while True:
    line = get_line()
    print("line", line)
    if line is None: break
    count, frm, to = parse_line(line)
    frm -= 1
    to -= 1
    stack_vals[to].extend(stack_vals[frm][-count:])
    for _ in range(count):
        stack_vals[frm].pop()

print(''.join([t[-1] for t in stack_vals]))

    