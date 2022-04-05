import sys
sys.stdin = open('input.txt')

def dijkstra(x):
    dist[x] = 0
    for _ in range(N):
        min_idx = -1
        min_value = inf
        for i in range(N+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1
        for j in range(N+1):
            if g[min_idx][j] and not visited[j]:
                if dist[min_idx] + g[min_idx][j] < dist[j]:
                    dist[j] = dist[min_idx] + g[min_idx][j]

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    inf = 987654321
    g = [[inf] * (N+1) for _ in range(N+1)]
    dist = [inf] * (N+1)
    visited = [0] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        g[s][e] = w
    dijkstra(0)
    print(f'#{tc} {dist[N]}')


