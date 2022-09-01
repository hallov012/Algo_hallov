import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = []
sx, sy = n, n
ex, ey = n, n
for i in range(n):
    row = input().rstrip()
    arr.append(row)
    for j in range(n):
        if arr[i][j] == '#':
            if (sx, sy) == (n, n):
                sx, sy = i, j
            else:
                ex, ey = i, j
# 북, 남, 동, 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
que = deque()
for i in range(4):
    que.append((sx, sy, i))
    visited[sx][sy][i] = 0

while que:
    x, y, dir = que.popleft()
    if x == ex and y == ey:
        print(visited[x][y][dir])
        break
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n:
        # 벽이 아닐 때
        if arr[nx][ny] != '*':
            if visited[nx][ny][dir] == -1 or visited[nx][ny][dir] > visited[x][y][dir]:
                visited[nx][ny][dir] = visited[x][y][dir]
                que.appendleft((nx, ny, dir))
            if arr[nx][ny] == '!':
                if dir < 2:
                    dir_lst = range(2, 4)
                else:
                    dir_lst = range(2)
                for ndir in dir_lst:
                    if visited[nx][ny][ndir] == -1 or visited[nx][ny][ndir] > visited[x][y][dir]+1:
                        visited[nx][ny][ndir] = visited[x][y][dir]+1
                        que.append((nx, ny, ndir))