import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = [0] * 31
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            t = arr[i][j]
            que = deque([(i, j)])
            visited[i][j] = True
            tmp = 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not visited[nx][ny] and arr[nx][ny] == t:
                            tmp += 1
                            visited[nx][ny] = True
                            que.append((nx, ny))
            if tmp >= k:
                cnt[t] += 1

max_cnt = 0
ans = -1
for i in range(30, 0, -1):
    if cnt[i] > max_cnt:
        max_cnt, ans = cnt[i], i

print(ans)