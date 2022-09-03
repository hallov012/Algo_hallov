import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for next in g[now]:
            if dist[next] > dist[now] + 1:
                dist[next] = dist[now] + 1
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
dist = dijkstra(x)
ans = []
for i in range(1, n+1):
    if dist[i] == k:
        ans.append(i)
if ans:
    for num in ans:
        print(num)
else:
    print(-1)