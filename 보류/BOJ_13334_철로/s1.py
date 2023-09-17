import sys, heapq
sys.stdin = open('input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

roads = []
for h, o in data:
    if abs(h-o) > d:
        continue
    if o > h:
        heapq.heappush(roads, (o, h))
    else:
        heapq.heappush(roads, (h, o))

while roads:
    h, o = heapq.heappop(roads)
    print()