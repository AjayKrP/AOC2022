ROCK=1
PAPER=2
SCISSORS=3

OPPONENT_MAPPING= {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
MY_MAPPING={'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}

def get_score(choice1, choice2):
    v1 = OPPONENT_MAPPING[choice1]
    v2 = MY_MAPPING[choice2]
    result = v2
    if v1 == v2:
        result += 3
    elif v1 == ROCK:
        if v2 == SCISSORS:
            result += 0
        else:
            result += 6
    elif v1 == SCISSORS:
        if v2 == PAPER:
            result += 0
        else:
            result += 6
    elif v1 == PAPER:
        if v2 == ROCK:
            result += 0
        else:
            result += 6
    return result

def part1():
    total = 0
    with open("input.txt") as file:
        for line in file:
            c1, c2 = line.rstrip().split(" ")
            total += get_score(c1, c2)
    return total

def choice_prediction(choice1, v2):
    v1 = OPPONENT_MAPPING[choice1]
    result = 0
    if v2 == 'Y':
        result = v1 + 3
    elif v2 == 'X':
        if v1 == ROCK:
            result = 3
        elif v1 == SCISSORS:
            result = 2
        elif v1 == PAPER:
            result = 1
    elif v2 == 'Z':
        if v1 == ROCK:
            result = 2
        elif v1 == SCISSORS:
            result = 1
        elif v1 == PAPER:
            result = 3
        result += 6
    return result



def part2():
    total = 0
    with open("input.txt") as file:
        for line in file:
            c1, c2 = line.rstrip().split(" ")
            total += choice_prediction(c1, c2)
    return total

print(part1())
print(part2())