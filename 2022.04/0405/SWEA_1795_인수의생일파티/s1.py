import sys
sys.stdin = open('input.txt')

def dijkstra(x):
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
    g = [[] for _ in range(n+1)]
    inf = 987654321
    dist = [inf] * (n+1)
    visited = [0] * (n+1)
    sum_lst = [0] * (n+1)
    for _ in range(m):
        s, e, w = map(int, input().split())
        g[s].append((e, w))
    for i in range(1, n+1):
        if i != x:
            dijkstra(i)
            sum_lst[i] = dist[x]
            dist = [inf] * (n+1)
            visited = [0] * (n+1)
    dijkstra(x)
    for j in range(1, n+1):
        if j != x:
            sum_lst[j] += dist[j]
    print(f'#{tc} {max(sum_lst)}')


