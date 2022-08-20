import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(start, end):
    dist = [sys.maxsize] * (n+1)
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
    return dist[end]

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
s, t = map(int, input().split())
print(dijkstra(s, t))