with open("input.txt") as file:
    matrix = []
    for line in file:
        lineArr = list(map(int, list(line.rstrip())))
        matrix.append(lineArr)

    m, n = len(matrix), len(matrix[0])
    total = (m * 2) + ((n - 2) * 2)  # count edges

    visible = set()

    def check_left(i, j, val):
        tmp = 0
        for k in range(i-1, -1, -1):
            tmp += 1
            if matrix[k][j] >= val:
                return False, tmp
        return True, tmp

    def check_right(i, j, val):
        tmp = 0
        for k in range(i+1, n):
            tmp += 1
            if matrix[k][j] >= val:
                return False, tmp
        return True, tmp

    def check_top(i, j, val):
        tmp = 0
        for k in range(j-1, -1, -1):
            tmp += 1
            if matrix[i][k] >= val:
                return False, tmp
        return True, tmp

    def check_bottom(i, j, val):
        tmp = 0
        for k in range(j+1, m):
            tmp += 1
            if matrix[i][k] >= val:
                return False, tmp
        return True, tmp

    score = float("-inf")

    for i in range(1, m-1):
        for j in range(1, n-1):
            val = matrix[i][j]
            res = 1
            w, a = check_left(i, j, val) # check if visible from left
            x, b = check_right(i, j, val) 
            y, c = check_bottom(i, j, val)
            z, d = check_top(i, j, val)

            score = max(score, a*b*c*d)
            if (i, j) not in visible and (x or y or w or z):
                visible.add((i, j))

    
    total += len(visible)

    print(total) # part 1
    print(score) # part 2
