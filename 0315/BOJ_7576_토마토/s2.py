import sys
from collections import deque
sys.stdin = open('input.txt')

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
end = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tomatos = deque()
stop_change = []
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomatos.append([i, j])
            end[i][j] = 1
while tomatos:
    x, y = tomatos.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not box[nx][ny] and not end[nx][ny]:
                end[nx][ny] = end[x][y] + 1
                box[nx][ny] = 1
                tomatos.append([nx, ny])

ans = max([max(line) for line in end]) - 1
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            ans = -1
            break
print(ans)
