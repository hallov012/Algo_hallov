import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = True
            que = deque([(i, j)])
            cnt += 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            que.append((nx, ny))

print(cnt)

