"""
                    [L]     [H] [W]
                [J] [Z] [J] [Q] [Q]
[S]             [M] [C] [T] [F] [B]
[P]     [H]     [B] [D] [G] [B] [P]
[W]     [L] [D] [D] [J] [W] [T] [C]
[N] [T] [R] [T] [T] [T] [M] [M] [G]
[J] [S] [Q] [S] [Z] [W] [P] [G] [D]
[Z] [G] [V] [V] [Q] [M] [L] [N] [R]
"""

import re

stacks = [
    ['Z', 'J', 'N', 'W', 'P', 'S'],
    ['G', 'S', 'T'],
    ['V', 'Q', 'R', 'L', 'H'],
    ['V', 'S', 'T', 'D'],
    ['Q', 'Z', 'T', 'D', 'B', 'M', 'J'],
    ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L'],
    ['L', 'P', 'M', 'W', 'G', 'T', 'J'],
    ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H'],
    ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
]


def parse_input():
    choice = []
    with open("input.txt") as file:
        for line in file:
            total, src, dst = list(map(int, re.findall(r"\d+", line.rstrip())))
            choice.append([total, src, dst])
    return choice


def part1():
    choices = parse_input()
    for choice in choices:
        total, src, dst = choice
        while total > 0:
            tmp = stacks[src - 1].pop()
            stacks[dst - 1].append(tmp)
            total -= 1
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result


def part2():
    choices = parse_input()
    for choice in choices:
        total, src, dst = choice
        tmpArr = stacks[src-1]
        lastItems = tmpArr[-total:]
        beginingItems = tmpArr[:-total]
        stacks[src - 1] = beginingItems
        stacks[dst - 1].extend(lastItems)
    result = ""
    for stack in stacks:
        result += stack[-1]
    return result


#print(''.join(part1()))
print(''.join(part2()))
