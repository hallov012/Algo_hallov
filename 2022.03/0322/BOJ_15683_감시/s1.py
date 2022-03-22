import sys
from itertools import combinations

sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = n * m
dx = [-1, 0, 1, 0]  # 상 좌 하 우
dy = [0, -1, 0, 1]
cctv = {0: [], 1: [[0], [1], [2], [3]], 2: [[0, 2], [1, 3], [0, 2], [1, 3]], 3: [[0, 3], [3, 2], [2, 1], [1, 0]],
        4: [[0, 3, 2], [3, 2, 1], [2, 1, 0], [1, 0, 3]], 5: [[0, 1, 2, 3]]}
k, all_k = 0, 0
for r in range(n):
    for c in range(m):
        if 0 < arr[r][c] < 6:
            all_k += 1
            if arr[r][c] < 5:
                k += 1

nums = [0, 1, 2, 3] * k
cases = list(combinations(nums, k))

for case in cases:
    cnt = n * m
    done = 0
    checked = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if 0 < arr[i][j] < 5:
                if not checked[i][j]:
                    cnt -= 1
                    checked[i][j] = 1
                for d in cctv[arr[i][j]][case[done]]:
                    x, y = i, j
                    while 0 <= x + dx[d] < n and 0 <= y + dy[d] < m and arr[x + dx[d]][y + dy[d]] != 6:
                        if not checked[x + dx[d]][y + dy[d]]:
                            checked[x + dx[d]][y + dy[d]] = 1
                            cnt -= 1
                        x += dx[d]
                        y += dy[d]
                done += 1
            if arr[i][j] == 5:
                if not checked[i][j]:
                    cnt -= 1
                    checked[i][j] = 1
                for d in cctv[5][0]:
                    x, y = i, j
                    while 0 <= x + dx[d] < n and 0 <= y + dy[d] < m and arr[x + dx[d]][y + dy[d]] != 6:
                        if not checked[x + dx[d]][y + dy[d]]:
                            checked[x + dx[d]][y + dy[d]] = 1
                            cnt -= 1
                        x += dx[d]
                        y += dy[d]
            elif arr[i][j] == 6:
                if not checked[i][j]:
                    cnt -= 1
                    checked[i][j] = 1
            if cnt - (all_k - done) * 2 * n > ans:
                break
    ans = min(ans, cnt)
print(ans)
