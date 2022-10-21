import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
arr = [[1] * m for _ in range(m)]
grow = [0] * (2 * m - 1)
for _ in range(n):
    a, b, c = map(int, input().split())
    for i in range(a, a+b):
        grow[i] += 1
    for i in range(a+b, 2*m-1):
        grow[i] += 2

for i in range(len(grow)):
    if i < m:
        arr[m-i-1][0] += grow[i]
    else:
        arr[0][i-m+1] += grow[i]
for i in range(1, m):
    for j in range(1, m):
        arr[i][j] = arr[0][j]
for line in arr:
    print(*line)