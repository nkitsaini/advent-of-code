# I do not use all the imports, but keep them if required
import sys
import itertools
import re
from pprint import pprint
from collections import *
import string
from typing import *


def main():
    # Raw Text
    content = sys.stdin.read()

    # each line stripped
    lines = [x.strip() for x in content.splitlines()]

    # each block (splitted by empty line)
    splits = content.split('\n\n')


    """
    I'll store nodes here like

    {
        11A: {
            left: 11B
            right: 11C
        },
        11B: {
            left: 11A
            right: 11Z
        },
        ...
    }
    
    """
    nodes = defaultdict(dict) # defaultdict is a very simple thing, just ask phind

    # First line contains instruction
    instructions = lines[0]

    # Start from second line to match the nodes
    for idx, line in enumerate(lines[2:]):
        # Two ways:
        # 1. Split using `=` sign, then remove `()` using `.strip()`, then again split using `,`
        # 2. Use regex (watch a video on regex, if you have never heard the name before)
        # Here I am using regex as you might already be familiar with approach 1 (which I had also used to solve the question initially)
        # 
        # **BEFORE GOING AHEAD**: Try to see what regex you will write to match the given into. Example: "abc = (xyz, ade)"

        # .* is always matching three characters here
        # We use paranthesis `()` to capture the values, whatever is in paranthesis, we can get it using match.groups(1) or match.groups(2)
        # "\(" and "\)" will match `)` and `(`. We are using `\` to tell regex that these are normal brackets not the captures/groups as above
        # `,` and ` ` (space) work as expected
        # Example "abc = (xyz, ade)"
        pattern = r"(.*) = \((.*), (.*)\)"
        match = re.fullmatch(pattern, line)

        # confirm that a match was found (as we expect)
        assert match is not None

        node = match.group(1)
        left = match.group(2)
        right = match.group(3)

        nodes[node] = {
            "left": left,
            "right": right
        }

    print(nodes)
    # At this point we have all the nodes in a dictionary
    # Now we'll just start following instructions to reach `ZZZ`

    """
    There are two ways to write the following.
    1. This is running instructions inside a loop, (which I had done for my initial solution)
    ```
    steps = 0
    while True:
        for instruction in instructions:
            steps += 1
            ...
            ...
            if value == 'ZZZ':
                print("Ans", steps)
                break
    ```

    2. Repeating the `instructions` using some help from python library. `itertools.cycle`
        - Read: https://docs.python.org/3/library/itertools.html
    ```
    for index, instruction in enumerate(itertools.cycle(instructions)):
        ...
        ...
        if match:
            print("Ans", i)
            break
        
    ```

    I am going to use second approach
    """

    current_node = "AAA"
    for index, instruction in enumerate(itertools.cycle(instructions)):
        print(current_node, instruction)
        if instruction == "R":
            current_node = nodes[current_node]['right']
        elif instruction == "L":
            current_node = nodes[current_node]['left']

        if current_node == "ZZZ":
            print("Answer", index + 1)
            break

    

if __name__ == "__main__":
    main()
