import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    g[a][b] = 1

for t in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][t] and g[t][j]:
                g[i][j] = 1

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if g[a][b]:
        print(-1)
    elif g[b][a]:
        print(1)
    elif not g[a][b]:
        print(0)