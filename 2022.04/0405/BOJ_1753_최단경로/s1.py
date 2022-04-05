import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra(x):
    dist[x] = 0
    for _ in range(V):
        min_idx = -1
        min_value = inf
        for i in range(1, V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1
        for e, w in g[min_idx]:
            if not visited[e]:
                if dist[min_idx] + w < dist[e]:
                    dist[e] = dist[min_idx] + w

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
inf = 987654321
g = defaultdict(list)
dist = [inf] * (V+1)
visited = [0] * (V+1)
for _ in range(E):
    s, e, w = map(int, input().split())
    g[s].append((e, w))
dijkstra(start)
for i in range(1, V+1):
    if dist[i] == inf:
        print('INF')
    else:
        print(dist[i])
