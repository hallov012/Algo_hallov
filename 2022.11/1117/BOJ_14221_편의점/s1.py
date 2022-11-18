import sys, heapq
from collections import defaultdict
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
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
p, q = map(int, input().split())
homes = sorted(list(map(int, input().split())))
stores = list(map(int, input().split()))
ans = n
min_dist = sys.maxsize
for store in stores:
    dist = dijkstra(store)
    for home in homes:
        if min_dist > dist[home]:
            ans = home
            min_dist = dist[home]
        elif min_dist == dist[home]:
            ans = min(ans, home)

print(ans)