import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

v, e = map(int, input().split())
g = [[sys.maxsize] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

ans = sys.maxsize
for i in range(1, v+1):
    ans = min(ans, g[i][i])

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
