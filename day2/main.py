ROCK=1
PAPER=2
SCISSOR=3

OPPONENT_MAPPING={'A': ROCK, 'B': PAPER, 'C': SCISSOR}
MY_CHOICE={'X': ROCK, 'Y': PAPER, 'Z': SCISSOR}

def check_score(choice1, choice2):
    v1 = OPPONENT_MAPPING[choice1]
    v2 = MY_CHOICE[choice2]

    result = v2
    if v1 == v2:
        result += 3
    elif (v1 == ROCK and v2 == SCISSOR) or \
        (v1 == SCISSOR and v2 == PAPER) or \
        (v1 == PAPER and v2 == ROCK):
        result += 0
    else:
        result += 6

    return result


def part1():
    total = 0
    with open("input.txt") as file:
        for line in file:
            c1, c2 = line.rstrip().split(" ")
            total += check_score(c1, c2)
    return total



def predict_next_move(choice1, choice2):
    v1 = OPPONENT_MAPPING[choice1]

    result = 0
    if choice2 == "Y":
        return v1 + 3 # draw score
    elif choice2 == "X":
        if v1 == ROCK:
            result = SCISSOR
        elif v1 == SCISSOR:
            result = PAPER
        elif v1 == PAPER:
            result = ROCK
        result += 0 # lose score
    elif choice2 == "Z":
        if v1 == ROCK:
            result = PAPER
        elif v1 == SCISSOR:
            result = ROCK
        elif v1 == PAPER:
            result = SCISSOR

        result += 6 # win score
    return result



def part2():
    total = 0
    with open("input.txt") as file:
        for line in file:
            c1, c2 = line.rstrip().split(" ")
            total += predict_next_move(c1, c2)
    return total


print(part1())
print(part2())
