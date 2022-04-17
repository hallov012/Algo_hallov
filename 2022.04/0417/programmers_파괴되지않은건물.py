def solution(board, skill):
    answer = 0
    n = len(skill)
    x = len(board)
    y = len(board[0])
    arr = [[0] * y for _ in range(x)]
    for i in range(n):
        type, r1, c1, r2, c2, degree = skill[i]
        if type == 1: # 공격
            arr[r1][c1] -= degree
            if r2+1 < x:
                arr[r2+1][c1] += degree
            if c2+1 < y:
                arr[r1][c2+1] += degree
            if r2+1 < x and c2+1 < y:
                arr[r2+1][c2+1] -= degree

        elif type == 2: # 회복
            arr[r1][c1] += degree
            if r2+1 < x:
                arr[r2+1][c1] -= degree
            if c2+1 < y:
                arr[r1][c2+1] -= degree
            if r2+1 < x and c2+1 < y:
                arr[r2+1][c2+1] += degree

    for i in range(x):
        for j in range(1, y):
            arr[i][j] += arr[i][j-1]
    for i in range(1, x):
        for j in range(y):
            arr[i][j] += arr[i-1][j]

    for i in range(x):
        for j in range(y):
            if board[i][j] + arr[i][j] > 0:
                answer += 1

    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
