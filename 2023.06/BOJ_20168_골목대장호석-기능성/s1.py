import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dijkstra(start):
    global ans
    q = []
    heapq.heappush(q, (0, 0, start))
    while q:
        max_cost, total_cost, now = heapq.heappop(q)
        if total_cost > c:
            continue
        for next, cost in g[now]:
            if total_cost + cost > c or visited[now][next]:
                continue
            elif next == b:
                ans = min(ans, max(max_cost, cost))
            visited[now][next] = 1
            heapq.heappush(q, (max(max_cost, cost), total_cost + cost, next))


n, m, a, b, c = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    p, q, k = map(int, input().split())
    g[p].append((q, k))
    g[q].append((p, k))
visited = [[0] * (n+1) for _ in range(n+1)]
ans = sys.maxsize
dijkstra(a)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)