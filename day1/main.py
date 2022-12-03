calories = []
from queue import PriorityQueue


def generateMaxHeap():
    totalCalory = 0
    calorySum = 0
    index = 0
    pq = PriorityQueue()
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                pq.put((-1 * calorySum, [totalCalory, index]))
                totalCalory = 0
                calorySum = 0
                index += 1
                continue
            
            totalCalory += 1
            calorySum += int(line.replace("\n", ""))
        return pq


def part1(q):
    if q.empty():
        return 0
    curr = q.get() # (-34324, [3. 6])
    return curr[0] * -1


def part2(q, r):
    total = r
    k = 2
    while k > 0:
        total += (q.get()[0] * -1)
        k-= 1
    return total


pq1 = generateMaxHeap()
res = part1(pq1)
print(f'part 1: {res}')
print(f"part2: {part2(pq1, res)}")
