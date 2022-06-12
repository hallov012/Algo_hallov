import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [inf] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        for b, c in g[now]:
            if dist[b] > dist[now] + c:
                dist[b] = dist[now] + c
                heapq.heappush(q, (dist[b], b))
    return dist

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n, d, h = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, c = map(int, input().split())
        g[b].append((a, c))
    inf = 987654321
    dist = dijkstra(h)
    ans = [0, 0]
    for i in range(1, n+1):
        if dist[i] != inf:
            ans[0] += 1
            ans[1] = max(ans[1], dist[i])
    print(*ans)


