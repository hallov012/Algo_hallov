import sys
sys.stdin = open('input.txt')

n = int(input())
strings = "abcdefghijklmnopqrstuvwxyz"
m = len(strings)
g = [[sys.maxsize] * m for _ in range(m)]

for _ in range(n):
    a, b = map(strings.index, input().rstrip().split(" is "))
    g[a][b] = 1

for k in range(m):
    for i in range(m):
        for j in range(m):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

k = int(input())
for _ in range(k):
    a, b = map(strings.index, input().rstrip().split(" is "))
    if g[a][b] == sys.maxsize:
        print('F')
    else:
        print('T')
