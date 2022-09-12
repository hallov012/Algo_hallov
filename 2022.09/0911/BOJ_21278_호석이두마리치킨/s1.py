import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    g[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

d_lst = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cnt = 0
        for k in range(1, n+1):
            if k not in (i, j):
                cnt += min(g[i][k], g[j][k])
        d_lst.append((i, j, cnt*2))
d_lst.sort(key=lambda x: x[2])
print(*d_lst[0])
