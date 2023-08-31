import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    heapq.heappush(g[s], e)
    heapq.heappush(g[e], s)

visited = [0] * (n+1)
visited[k] = 1
while True:
    flag = False
    while g[k]:
        next = heapq.heappop(g[k])
        if not visited[next]:
            visited[next] += visited[k] + 1
            k = next
            flag = True
            break
    if not flag:
        break

print(visited[k], k)