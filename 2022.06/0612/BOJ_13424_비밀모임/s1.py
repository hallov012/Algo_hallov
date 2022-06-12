import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
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
    return dist

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    inf = 987654321
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a].append((b, c))
        g[b].append((a, c))
    k = int(input())
    rooms = list(map(int, input().split()))
    total_dist = [0] * (n+1)
    for room in rooms:
        dist = dijkstra(room)
        for j in range(1, n+1):
            total_dist[j] += dist[j]
    ans = 0
    min_sum = 10 ** 5
    for i in range(1, n+1):
        if total_dist[i] < min_sum:
            min_sum = total_dist[i]
            ans = i
    print(ans)

