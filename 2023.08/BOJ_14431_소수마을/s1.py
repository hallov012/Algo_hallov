import sys, math, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def digkstra(start):
    dist = [sys.maxsize] * (n+2)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for next, c in g[now]:
            if dist[next] > d + c:
                dist[next] = d + c
                heapq.heappush(q, (dist[next], next))
    return dist

input = sys.stdin.readline

m = int(math.sqrt(2 * ((3000 * 2) ** 2)))
nums = [True] * (m+1)
nums[0] = nums[1] = False
for i in range(2, int(math.sqrt(m)) + 1):
    if nums[i]:
        for j in range(2*i, m+1, i):
            nums[j] = False

x1, y1, x2, y2 = map(int, input().split())
n = int(input())
g = defaultdict(list)
locations = [(x1, y1)]
for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))
locations.append((x2, y2))

for i in range(n+1):
    a1, b1 = locations[i]
    for j in range(i+1, n+2):
        a2, b2 = locations[j]
        d = math.trunc(math.sqrt((a1-a2)**2 + (b1-b2)**2))
        if nums[d]:
            g[i].append((j, d))
            g[j].append((i, d))

dist = digkstra(0)
if dist[-1] == sys.maxsize:
    print(-1)
else:
    print(dist[-1])
