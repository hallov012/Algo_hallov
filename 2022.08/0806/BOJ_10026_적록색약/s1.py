import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
not_weakness = [[0] * n for _ in range(n)]
color_weakness = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

not_weakness_cnt = 0
for i in range(n):
    for j in range(n):
        if not not_weakness[i][j]:
            color = arr[i][j]
            not_weakness_cnt += 1
            not_weakness[i][j] = 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == color and not not_weakness[nx][ny]:
                            not_weakness[nx][ny] = 1
                            que.append((nx, ny))

color_weakness_cnt = 0
for i in range(n):
    for j in range(n):
        if not color_weakness[i][j]:
            color = arr[i][j]
            color_weakness_cnt += 1
            color_weakness[i][j] = 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if color == 'B':
                            if arr[nx][ny] == color and not color_weakness[nx][ny]:
                                color_weakness[nx][ny] = 1
                                que.append((nx, ny))
                        else:
                            if arr[nx][ny] != 'B' and not color_weakness[nx][ny]:
                                color_weakness[nx][ny] = 1
                                que.append((nx, ny))
print(not_weakness_cnt, color_weakness_cnt)




