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
        for next, x in g[now]:
            if dist[next] > d + x:
                dist[next] = d + x
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n = int(input())
a, b, c = (map(int, input().split()))
m = int(input())
g = defaultdict(list)
for _ in range(m):
    d, e, l = map(int, input().split())
    g[d].append((e, l))
    g[e].append((d, l))

a_dist = dijkstra(a)
b_dist = dijkstra(b)
c_dist = dijkstra(c)

ans = 0
max_num = 0
for i in range(1, n+1):
    min_num = min(a_dist[i], b_dist[i], c_dist[i])
    if min_num > max_num:
        max_num = min_num
        ans = i

print(ans)
