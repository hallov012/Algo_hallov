import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            if dist[next] > dist[now] + cost and not check[next]:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
check = list(map(int, input().split()))
check[-1] = 0
for _ in range(m):
    a, b, t = map(int, input().split())
    g[a].append((b, t))
    g[b].append((a, t))

dist = dijkstra(0)
if dist[n-1] != sys.maxsize:
    print(dist[n-1])
else:
    print(-1)