import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra(start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = K
    q = []
    heapq.heappush(q, (K, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, l in graph[now]:
            for x, s, e in cant_go[now]:
                if x == next:
                    # 지나가고 있으면 기다림
                    if s <= d < e:
                        if dist[next] > e+l:
                            dist[next] = e+l
                            heapq.heappush(q, (dist[next], next))
                    # 아니면 그냥 지나감
                    else:
                        if dist[next] > d+l:
                            dist[next] = d+l
                            heapq.heappush(q, (dist[next], next))
                    break
            else:
                if dist[next] > d+l:
                    dist[next] = d+l
                    heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

n, m = map(int, input().split())
A, B, K, G = map(int, input().split())
cross = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

cant_go = defaultdict(list)
t = 0
for i in range(G-1):
    now, next = cross[i], cross[i+1]
    for a, b in graph[now]:
        if a == next:
            cant_go[now].append((next, t, t+b))
            cant_go[next].append((now, t, t+b))
            t += b
            break
dist = dijkstra(A)
print(dist[B] - K)







