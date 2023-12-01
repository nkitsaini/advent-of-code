from typing import *
from functools import cache
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

@cache
def _sub_helper(remains: Tuple[int]) -> int:
    all_divs = [m.test_div for m in monkeys]
    # print(remains)
    for subs in range(1, 100000000):
        remains_ = tuple(subs%d for d in all_divs)
        if remains_ == remains:
            return subs

def get_substitute(value: int) -> int:
    all_divs = [m.test_div for m in monkeys]
    remains = [value%d for d in all_divs]
    return _sub_helper(tuple(remains))
    # for subs in range(1, 100000):
    #     remains_ = [subs%d for d in all_divs]
    #     if remains_ == remains:
    #         return subs


@dataclass
class Monkey:
    id: int
    items: List[int]
    opr: str
    test_div: int
    test_true_monkey: int
    test_false_monkey: int

    def operate(self, i: int) -> int:
        old = self.items[i]
        opr = self.opr.replace('new = ', '')
        new = eval(opr.strip())
        if 'old * old' in self.opr:
            new = get_substitute(new)
            # all_divs = [m.test_div for m in monkeys]
            # remains = [new%d for d in all_divs]
            # for subs in range(1, 100000):
            #     remains_ = [subs%d for d in all_divs]
            #     if remains_ == remains:
            #         new = subs
            #         break
        self.items[i] = new
    
ans = 0

monkeys: List[Monkey] = []
while True:

    line = get_line()
    if line is None: break

    mid = int(line[:-1].split()[-1])

    line = get_line()
    items = list(map(int, line.split(':')[-1].split(',')))

    line = get_line()
    opr = line.split(':')[-1]

    line = get_line()
    test_div = int(line.split(' ')[-1])

    line = get_line()
    true_monkey = int(line.split(' ')[-1])

    line = get_line()
    false_monkey = int(line.split(' ')[-1])

    monkeys.append(
        Monkey(id=mid, items=items, opr=opr, test_div=test_div, test_true_monkey=true_monkey, test_false_monkey=false_monkey)
    )
    get_line() # empty line
    if line is None: break


inspect_counts = defaultdict(int)
pprint(monkeys)
for rid in range(10000):
    print("===================", rid)
    for mid, monkey in  enumerate(monkeys):
        for i, _ in enumerate(monkey.items):
            inspect_counts[mid] += 1
            monkey.operate(i)
            # monkey.items[i] //= 3
            test_val = (monkey.items[i] % (monkey.test_div)) == 0
            if test_val:
                # print("Throwing", monkey.items[i], "to monkey", monkey.test_true_monkey)
                monkeys[monkey.test_true_monkey].items.append(monkey.items[i])
            else:
                # print("Throwing", monkey.items[i], "to monkey", monkey.test_false_monkey)
                monkeys[monkey.test_false_monkey].items.append(monkey.items[i])
        print("DONE MONEKY", mid)
        monkey.items = []

print(inspect_counts)
two_max = sorted(inspect_counts.values())[-2:]
print(two_max[0]*two_max[1])
print("ans", ans)

    



