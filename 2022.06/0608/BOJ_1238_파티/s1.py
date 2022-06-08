# heap을 이용한 dijikstra
import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s):
    q = []
    dist = [inf] * (n+1)
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for b, c in g[now]:
            cost = d + c
            if dist[b] > cost:
                dist[b] = cost
                heapq.heappush(q, (cost, b))
    return dist

input = sys.stdin.readline

n, m, x = map(int, input().split())
g = [[] for _ in range(n+1)]
inf = 987654321

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

ans = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x] + back[i])

print(ans)