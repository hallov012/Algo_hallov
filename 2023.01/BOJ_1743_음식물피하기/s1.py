import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
visited = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            que = deque([(i, j)])
            cnt = 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            cnt += 1
                            que.append((nx, ny))
            if cnt > ans:
                ans = cnt

print(ans)