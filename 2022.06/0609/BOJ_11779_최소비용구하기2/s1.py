import sys, heapq
sys.stdin = open('input.txt')

def dijckstra(start):
    dist = [[inf, []] for _ in range(n+1)]
    dist[start] = [0, [start]]
    q = []
    heapq.heappush(q, (0, start, [start]))
    while q:
        cost, now, route = heapq.heappop(q)
        if dist[now][0] < cost:
            continue
        for b, c in g[now]:
            if dist[b][0] > dist[now][0] + c:
                dist[b][0] = dist[now][0] + c
                new_route = route[::]
                new_route.append(b)
                heapq.heappush(q, (dist[b][0], b, new_route))
                dist[b][1] = new_route
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
ans = dijckstra(start)
print(ans[end][0])
print(len(ans[end][1]))
print(*ans[end][1])

