import sys, heapq
sys.stdin = open('input.txt')

def dijkstra():
    dist = [sys.maxsize] * (target + 1)
    dist[0] = 0
    q = []
    heapq.heappush(q, (0, 0))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in g[now]:
            if dist[next] > d + cost:
                dist[next] = d + cost
                heapq.heappush(q, (dist[next], next))
    return dist[target]

input = sys.stdin.readline

n, target = map(int, input().split())
g = [[] for _ in range(target+1)]

for i in range(target):
    g[i].append((i+1, 1))

for i in range(n):
    a, b, c = map(int, input().split())
    if b <= target:
        g[a].append((b, c))

ans = dijkstra()
print(ans)