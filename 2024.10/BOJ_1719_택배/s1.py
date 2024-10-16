import sys
sys.stdin = open('imput.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[sys.maxsize] * (n+1) for _ in range(n+1)]
ans = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    g[i][i] = 0
    ans[i][i] = '-'

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = g[b][a] = c
    ans[a][b] = b
    ans[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            tmp = g[i][k] + g[k][j]
            if g[i][j] > tmp:
                g[i][j] = tmp
                ans[i][j] = ans[i][k]

for i in range(1, n+1):
    print(*ans[i][1:])