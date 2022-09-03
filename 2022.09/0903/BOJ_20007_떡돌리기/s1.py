import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, m, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = dijkstra(y)
dist.sort()
if max(dist) * 2 > x:
    print(-1)
else:
    ans = 1
    i = 0
    day = x
    while i < n:
        if day - dist[i] * 2 >= 0:
            day -= dist[i] * 2
        else:
            ans += 1
            day = x - dist[i] * 2
        i += 1
    print(ans)

