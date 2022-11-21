import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
p, q = map(int, input().split())
homes = list(map(int, input().split()))
stores = list(map(int, input().split()))
dist = [sys.maxsize] * (n + 1)
q = []
for store in stores:
    dist[store] = 0
    heapq.heappush(q, (0, store))
while q:
    d, now = heapq.heappop(q)
    if now in homes:
        print(now)
        break
    if dist[now] < d:
        continue
    for next, c in g[now]:
        if dist[next] > dist[now] + c:
            dist[next] = dist[now] + c
            heapq.heappush(q, (dist[next], next))
