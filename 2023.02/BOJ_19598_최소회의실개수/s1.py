import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
rooms = [0]
for start, end in arr:
    time = heapq.heappop(rooms)
    if start >= time:
        heapq.heappush(rooms, end)
    else:
        heapq.heappush(rooms, time)
        heapq.heappush(rooms, end)
print(len(rooms))
