import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 987654321
g = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    g[s][e] = min(d, g[s][e])

for k in range(1, n+1):
    g[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if g[i][j] == inf:
            print(0, end=' ')
        else:
            print(g[i][j], end=' ')
    print()
