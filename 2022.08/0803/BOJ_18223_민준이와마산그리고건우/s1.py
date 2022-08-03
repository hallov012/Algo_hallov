import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (v+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            if dist[next] > d + cost:
                dist[next] = d + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

v, e, p = map(int, input().split())
g = [[] for _ in range(v+1)]
path = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

start_dist = dijkstra(1)
help_dist = dijkstra(p)

if start_dist[v] == start_dist[p] + help_dist[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
