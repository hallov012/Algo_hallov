import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s):
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
    return dist

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
g = [[] for _ in range(n+1)]
inf = 987654321
for _ in range(r):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

ans = 0
for i in range(1, n+1):
    dist_return = dijkstra(i)
    cnt = 0
    for j in range(1, n+1):
        if dist_return[j] <= m:
            cnt += items[j]
    ans = max(ans, cnt)

print(ans)