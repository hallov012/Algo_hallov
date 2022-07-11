import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
data = [input().strip() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 'L':
            visited = [[0] * m for _ in range(n)]
            cnt = 0
            visited[i][j] = 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if not visited[nx][ny] and data[nx][ny] == 'L':
                            visited[nx][ny] = visited[x][y] + 1
                            cnt = max(cnt, visited[nx][ny])
                            que.append((nx, ny))
            ans = max(ans, cnt-1)
print(ans)


