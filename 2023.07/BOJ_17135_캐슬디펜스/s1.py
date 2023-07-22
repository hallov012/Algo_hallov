import sys, copy
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 아래로 탐색할 필요는 없음
dx = [0, -1, 0]
dy = [-1, 0, 1]

ans = 0
cases = list(combinations(range(m), 3))

for case in cases:
    temp_arr = copy.deepcopy(arr)
    killed = [[0] * m for _ in range(n)]
    cnt = 0
    # 적군이 한칸씩 내려 오는 것을 따로 구현하지 않고 n-1에서 역순으로 for문을 돌려서 대체
    for i in range(n-1, -1, -1):
        temp = []
        for c in case:
            que = deque([(i, c, 1)])
            while que:
                x, y, dist = que.popleft()
                if temp_arr[x][y]:
                    if not killed[x][y]:
                        temp.append((x, y))
                        killed[x][y] = 1
                        cnt += 1
                    break
                if dist < d:
                    for j in range(3):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < n and 0 <= ny < m:
                            que.append((nx, ny, dist+1))
        for a, b in temp:
            temp_arr[a][b] = 0
    ans = max(ans, cnt)

print(ans)