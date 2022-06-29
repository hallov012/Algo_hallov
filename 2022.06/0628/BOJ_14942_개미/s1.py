"""
도착지 1로부터 dijkstra를 실행하여 각 방까지의 최단거리를 구하기
각 방으로 가는 경로를 dist에 저장해야할 것 같당...
"""
import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(s):
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for b, c in g[now]:
            if dist[b] > dist[now] + c:
                dist[b] = dist[now] + c
                path[b].append(now)
                heapq.heappush(q, (dist[b], b))
    return

input = sys.stdin.readline

n = int(input())
ant = [0] + [int(input()) for _ in range(n)]
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = [sys.maxsize] * (n + 1)
path = [[] for _ in range(n+1)]
dijkstra(1)

for i in range(2, n+1):
    for b, c in g[i]:
        if b == path[i][0]:
            path[i].append(c)

ans = [1]
for i in range(2, n+1):
    energy = ant[i]
    now = i
    while True:
        energy -= path[now][1]
        if energy < 0:
            ans.append(now)
            break
        now = path[now][0]
        if now == 1:
            ans.append(1)
            break

for num in ans:
    print(num)