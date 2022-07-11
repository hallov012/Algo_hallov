import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
path = [[[i] for _ in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if dist[a][b] == sys.maxsize:
        path[a][b].append(b)
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == 0 or dist[i][j] == sys.maxsize:
            print(0)
        else:
            print(len(path[i][j]), *path[i][j])

