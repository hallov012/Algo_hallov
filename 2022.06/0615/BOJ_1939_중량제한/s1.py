import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s, e):
    dist = [0] * (n+1)
    dist[s] = sys.maxsize
    q = []
    heapq.heappush(q, (-sys.maxsize, s))
    while q:
        d, now = heapq.heappop(q)
        d *= -1
        if d < dist[now]:
            continue
        for b, c in g[now]:
            if dist[b] < min(d, c):
                dist[b] = min(d, c)
                heapq.heappush(q, (-dist[b], b))
    return dist[e]

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))
s, e = map(int, input().split())
print(dijkstra(s, e))
