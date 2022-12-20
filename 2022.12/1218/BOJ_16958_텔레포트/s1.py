import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, t = map(int, input().split())
g = [[0] * n for _ in range(n)]
city = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    s, a, b = city[i]
    for j in range(i+1, n):
        k, c, d = city[j]
        dist = abs(a - c) + abs(b - d)
        if s == 1 and k == 1 and dist > t:
            g[i][j] = t
            g[j][i] = t
        else:
            g[i][j] = dist
            g[j][i] = dist

for p in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] > g[i][p] + g[p][j]:
                g[i][j] = g[i][p] + g[p][j]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(g[a-1][b-1])