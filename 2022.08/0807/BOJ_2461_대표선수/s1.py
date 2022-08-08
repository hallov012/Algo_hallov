import sys, heapq
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
student = [deque(sorted(list(map(int, input().split())))) for _ in range(n)]

que = []
min_n = sys.maxsize
max_n = 0

# 각 반의 최솟값을 que에 담음
for i in range(n):
    v = student[i].popleft()
    min_n = min(min_n, v)
    max_n = max(max_n, v)
    heapq.heappush(que, (v, i))

ans = max_n - min_n

while que:
    min_value, idx = heapq.heappop(que)
    # 만약 다음 최솟값을 찾을 수 없다면 break(갱신 불가능)
    if not student[idx]:
        break

    # 다음 최솟값을 찾아 que에 넣어준다
    new_value = student[idx].popleft()
    heapq.heappush(que, (new_value, idx))

    if max_n < new_value:
        max_n = new_value
    min_n = que[0][0]
    ans = min(ans, max_n - min_n)

print(ans)