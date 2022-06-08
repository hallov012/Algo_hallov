import sys, heapq
sys.stdin = open('input.txt')

def dijikstra(start, end):
    dist = [inf] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for b, c in g[now]:
            if dist[b] > dist[now] + c:
                dist[b] = dist[now] + c
                heapq.heappush(q, (dist[b], b))
    return dist[end]

input = sys.stdin.readline

n, e = map(int, input().split())
inf = 987654321
g = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
v1, v2 = map(int, input().split())

path1 = dijikstra(1, v1) + dijikstra(v1, v2) + dijikstra(v2, n)
path2 = dijikstra(1, v2) + dijikstra(v2, v1) + dijikstra(v1, n)

if path1 >= inf and path2 >= inf:
    print(-1)
else:
    print(min(path1, path2))