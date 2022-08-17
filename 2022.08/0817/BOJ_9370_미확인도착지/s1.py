import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, cost in graph[now]:
            if dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    gh_dist = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        if (a == g or b == h) or (a == h or b == g):
            gh_dist = c

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    ans = []
    for _ in range(t):
        end = int(input())
        if dist_s[end] == dist_s[h] + dist_h[g] + dist_g[end] or dist_s[end] == dist_s[g] + dist_g[h] + dist_h[end]:
            ans.append(end)
    ans.sort()
    print(*ans)



