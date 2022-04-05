import sys
sys.stdin = open('input.txt')

def dijkstra(x, g, dist):
    dist[x] = 0
    for _ in range(n):
        min_idx = -1
        min_value = inf
        for i in range(1, n+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1
        for e, w in g[min_idx]:
            if not visited[e] and dist[min_idx] + w < dist[e]:
                dist[e] = dist[min_idx] + w

T = int(input())

for tc in range(1, T+1):
    n, m, x = map(int, input().split())
    g_True = [[] for _ in range(n+1)]
    g_reverse = [[] for _ in range(n + 1)]
    inf = 987654321
    dist_True = [inf] * (n+1)
    dist_reverse = [inf] * (n+1)
    visited = [0] * (n+1)
    sum_lst = [0] * (n+1)
    for _ in range(m):
        s, e, w = map(int, input().split())
        g_True[s].append((e, w))
        g_reverse[e].append((s, w))
    dijkstra(x, g_True, dist_True)
    visited = [0] * (n+1)
    dijkstra(x, g_reverse, dist_reverse)
    for i in range(1, n+1):
        sum_lst[i] = dist_True[i] + dist_reverse[i]
    print(f'#{tc} {max(sum_lst)}')