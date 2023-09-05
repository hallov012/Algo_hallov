import sys, heapq
from collections import defaultdict
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
        for next, c in g[now]:
            if dist[next] > d + c:
                dist[next] = d + c
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, v, e = map(int, input().split())
a, b = map(int, input().split())
h_lst = list(map(int, input().split()))
g = defaultdict(list)
for _ in range(e):
    x, y, l = map(int, input().split())
    g[x].append((y, l))
    g[y].append((x, l))

ans = 0
for h in h_lst:
    dist = dijkstra(h)
    x, y = dist[a], dist[b]
    if dist[a] == sys.maxsize:
        dist[a] = -1
    if dist[b] == sys.maxsize:
        dist[b] = -1
    ans += (x + y)

print(ans)


