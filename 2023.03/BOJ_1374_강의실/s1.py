import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
courses = [list(map(int, input().split())) for _ in range(n)]
courses.sort(key=lambda x: x[1])
rooms = [0]
for num, start, end in courses:
    if rooms[0] <= start:
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    else:
        heapq.heappush(rooms, end)
print(len(rooms))