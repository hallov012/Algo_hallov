import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    u, v, b = map(int, input().split())
    dist[u][v] = 0
    if b == 0:
        dist[v][u] = 1
    else:
        dist[v][u] = 0

for t in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j])

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(dist[s][e])



