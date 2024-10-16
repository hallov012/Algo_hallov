import sys, heapq
from collections import defaultdict
sys.stdin = open('imput.txt')

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

ans = []
for i in range(1, n+1):
    dist = [sys.maxsize] * (n+1)
    dist[i] = 0
    row = [0] * (n+1)
    q = [(0, i)]
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            tmp = dist[now] + c
            if dist[next] > tmp:
                dist[next] = tmp
                row[next] = now
                heapq.heappush(q, (dist[next], next))
    row[i] = '-'
    print(*row[1:])



