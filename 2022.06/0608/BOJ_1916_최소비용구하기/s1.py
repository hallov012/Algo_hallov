import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s):
    dist = [inf] * (n+1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]:
            continue
        for b, c in g[now]:
            if dist[b] > dist[now] + c:
                dist[b] = dist[now] + c
                heapq.heappush(q, (dist[b], b))
    return dist

input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
inf = 987654321
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
start, end = map(int, input().split())

ans = dijkstra(start)
print(ans[end])
