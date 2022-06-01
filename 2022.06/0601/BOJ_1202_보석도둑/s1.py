# 우선순위 큐
import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
gems = []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(gems, [w, v])
bag = []
for _ in range(k):
    heapq.heappush(bag, int(input()))

ans = 0
possible = []

for _ in range(k):
    capacity = heapq.heappop(bag)
    while gems and capacity >= gems[0][0]:
        w, v = heapq.heappop(gems)
        heapq.heappush(possible, -v)  # 내림차순 정렬이 되어야하므로 -를 붙여 음수로 넣어준다
    if possible:
        ans -= heapq.heappop(possible)
    elif not gems:
        break

print(ans)
