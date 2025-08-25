import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
stations = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(stations, (a, -b))
l, p = map(int, input().split())
heapq.heappush(stations, (l, 0))

passed = []
d_move, now = 0, 0
ans = 0
while stations:
    a, b = heapq.heappop(stations)
    d_move = a - now
    # 움직이지 못하는 경우 지나온 곳 중 제일 많이 충전 가능한 곳에서 충전...
    if d_move > p:
        while passed and p < d_move:
            g = heapq.heappop(passed)
            p += -g
            ans += 1
        if d_move > p:
            ans = -1
            break
        else:
            p -= d_move
            now = a
    heapq.heappush(passed, b)

print(ans)