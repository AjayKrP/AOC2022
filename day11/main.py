from collections import deque
from math import gcd, prod
from operator import floordiv, mod
class Ops:
    def __init__(self, operator, value) -> None:
        self.operator = operator
        self.value = value
        
class Monkey:
    def __init__(self, id=0, items=None, ops= None, test=None, action=[]) -> None:
        self.id = id
        self.items = items
        self.ops = ops
        self.test = test
        self.action = action
    

def parse_input():
    monkeys = []
    monkey = None
    id = -1
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if 'Monkey' in line:
                id += 1
                monkey = Monkey(id=id)
                monkey.total = 0
                monkey.action = []
            elif 'Starting items' in line:
                currentItems = list(map(int, line.split(":")[1].strip().split(",")))
                monkey.items = deque(currentItems)
            elif 'Operation' in line:
                operation = line.split("=")[1].strip()
                operator = None
                operands = None
                if "+" in operation:
                    operator = "+"
                    operands = operation.split("+")
                else:
                    operator = "*"
                    operands = operation.split("*")
                
                monkey.ops = Ops(operator, operands)
            elif "Test" in line:
                test = int(line.split()[-1])
                monkey.test = test
            elif "If true" in line:
                val = int(line.split()[-1])
                monkey.action.append(val)
            elif "If false" in line:
                val = int(line.split()[-1])
                monkey.action.append(val)
            elif line == "":
                monkeys.append(monkey)
    return monkeys
    
def perform_operation(sign, old, new):
    if sign == "+":
        return old + new
    elif sign == "*":
        return old * new

def solve(monkeys, T, div, _op):
    while T > 0:
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey.total += 1
                ops = monkey.ops
                op1, op2 = ops.value
                op1 = op1.strip()
                op2 = op2.strip()
                if op1 == "old":
                    op1 = item
                else:
                    op1 = int(op1)
                if op2 == "old":
                    op2 = item
                else:
                    op2 = int(op2)
                
                currentVal = _op(perform_operation(ops.operator, op1, op2), div)
                
                if currentVal % monkey.test == 0:
                    monkeys[monkey.action[0]].items.append(currentVal)
                else:
                    monkeys[monkey.action[1]].items.append(currentVal)
        T -= 1

    tmp = []
    for monkey in monkeys:
        tmp.append(monkey.total)
    tmp.sort()
    return tmp[-1]*tmp[-2]
            


monkeys = parse_input()
#print(solve(monkeys, 20, 3, floordiv)) # part 1

div = 1
for m in monkeys:
    div *= m.test

print(solve(monkeys, 10000,  div, mod)) # part 2

