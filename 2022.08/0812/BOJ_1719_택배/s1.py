import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
path = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)
    path[a][b] = b
    path[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                path[i][j] = path[i][k]

for i in range(1, n+1):
    path[i][i] = '-'

for i in range(1, n+1):
    line = path[i]
    print(*line[1:])