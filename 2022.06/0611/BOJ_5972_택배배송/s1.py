import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s, e):
    dist = [inf] * (n+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for b, c in g[now]:
            if dist[b] > dist[now] + c:
                dist[b] = dist[now] + c
                heapq.heappush(q, (dist[b], b))
    return dist[e]

input = sys.stdin.readline

n, m = map(int, input().split())
inf = 987654321
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

ans = dijkstra(1, n)
print(ans)