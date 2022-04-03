import sys
sys.stdin = open('input.txt')

def dijkstra(x):
    distance[x] = 0
    for _ in range(n + 1):
        min_idx = -1
        min_val = inf
        for i in range(n + 1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1
        for j in range(n + 1):
            if g[min_idx][j] and not visited[j]:
                if distance[min_idx] + g[min_idx][j] < distance[j]:
                    distance[j] = distance[min_idx] + g[min_idx][j]



T = int(input())

for tc in range(1, T+1):
    n, e = map(int, input().split())
    inf = 987654321
    g = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(e):
        start, end, d = map(int, input().split())
        g[start][end] = d
    distance = [inf] * (n + 1)
    visited = [0] * (n + 1)
    start = 0
    dijkstra(0)
    print(f'#{tc} {distance[n]}')
