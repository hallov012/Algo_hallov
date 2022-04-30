import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato_box = []
que = deque()
for k in range(h):
    box = []
    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(m):
            if line[j] == 1:
                que.append((k, i, j))
        box.append(line)
    tomato_box.append(box)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
while que:
    box, x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato_box[box][nx][ny] == 0:
                tomato_box[box][nx][ny] = tomato_box[box][x][y] + 1
                que.append((box, nx, ny))
    for i in (-1, 1):
        if 0 <= box + i < h:
            if tomato_box[box+i][x][y] == 0:
                tomato_box[box+i][x][y] = tomato_box[box][x][y] + 1
                que.append((box+i, x, y))

flag = True
ans = 0
for box in tomato_box:
    for line in box:
        if 0 in line:
            flag = False
            break
        ans = max(max(line), ans)

if flag:
    print(ans-1)
else:
    print(-1)


