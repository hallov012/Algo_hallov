import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
heap = []
rooms = []
for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(heap, (s, t))
heapq.heappush(rooms, heapq.heappop(heap)[1])
while heap:
    start, end = heapq.heappop(heap)
    if start >= rooms[0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    else:
        heapq.heappush(rooms, end)
print(len(rooms))