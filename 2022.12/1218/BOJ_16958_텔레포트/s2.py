import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, t = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
g = [[0] * n for _ in range(n)]
for i in range(n-1):
    s1, x1, y1 = city[i]
    for j in range(i+1, n):
        s2, x2, y2 = city[j]
        dist = abs(x1-x2) + abs(y1-y2)
        if s1 == s2 == 1 and dist > t:
            g[i][j] = t
        else:
            g[i][j] = dist

for k in range(n):
    for i in range(n-1):
        for j in range(i+1, n):
            if k <= i:
                g[i][j] = min(g[i][j], g[k][i] + g[k][j])
            elif i < k <= j:
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
            else:
                g[i][j] = min(g[i][j], g[i][k] + g[j][k])

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if a < b:
        print(g[a-1][b-1])
    else:
        print(g[b-1][a-1])