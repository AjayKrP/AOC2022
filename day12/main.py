
from queue import Queue

with open("input.txt") as file:
    matrix = []

    S = None
    E = None
    i = 0
    for line in file:
        currentLine = line.strip()
        if "E" in currentLine:
            E = ((i, currentLine.index("E")), 0)
        if "S" in currentLine:
            S = ((i, currentLine.index("S")), 0)
        matrix.append(list(currentLine))

        i += 1

    i = 0
    m, n = len(matrix), len(matrix[0])
    q = Queue()


    def find_all_lowest_point():
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "S" or matrix[i][j] == "a":
                    yield ((i, j), 0)

    def bfs(S):
        visited = set()
        for position in S:
            q.put(position)
            visited.add(position)
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while not q.empty():
            curr = q.get()
            currentValue = matrix[curr[0][0]][curr[0][1]]
            if currentValue == "E":
                print(curr[1])
                return
            
            if (currentValue == "S"):
                currentValue = "a"
        
            for d in dir:
                cx = d[0] + curr[0][0]
                cy = d[1] + curr[0][1]                
                if cx >= m or cx < 0 or cy >= n or cy < 0:
                    continue
                elem = matrix[cx][cy]
                if elem == "E":
                    elem = "z"

                if (cx, cy) not in visited and ord(elem) <= ord(currentValue) + 1:
                    visited.add((cx, cy))
                    q.put(((cx, cy), curr[1] + 1))

    #bfs([S]) # part 1

    start_positions = list(find_all_lowest_point())
    bfs(start_positions)
