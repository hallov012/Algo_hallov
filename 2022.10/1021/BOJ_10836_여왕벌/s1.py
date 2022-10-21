import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [[[1, 0] for _ in range(m)] for _ in range(m)]
for _ in range(n):
    data = list(map(int, input().split()))
    grow = []
    for i in range(3):
        grow.extend([i] * data[i])
    for i in range(len(grow)):
        if i < m:
            arr[m-i-1][0][0] += grow[i]
            arr[m-i-1][0][1] = grow[i]
        else:
            arr[0][i-m+1][0] += grow[i]
            arr[0][i-m+1][1] = grow[i]
    for i in range(1, m):
        for j in range(1, m):
            temp = max(arr[i][j-1][1], arr[i-1][j-1][1], arr[i-1][j][1])
            arr[i][j][0] += temp
            arr[i][j][1] = temp
for line in arr:
    row = []
    for x, y in line:
        row.append(x)
    print(*row)