import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
swan = 1
water = deque()
visited = [[0] * c for _ in range(r)]
swans = deque()
for i in range(r):
    line = list(map(str, input().strip()))
    for j in range(c):
        if line[j] == '.':
            water.append((i, j))
        elif line[j] == 'L':
            line[j] = '.'
            water.append((i, j))
            visited[i][j] = swan
            swans.append((i, j))
            swan += 1
    arr.append(line)

ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while swans:
    x, y = swans.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == '.':
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y]
                    swans.append((nx, ny))
                elif visited[nx][ny] != visited[x][y]:
                    print(ans)
                    exit()

while True:
    flag = False
    ans += 1
    new_water = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] == 'X':
                    arr[nx][ny] = '.'
                    new_water.append((nx, ny))
                    visited[nx][ny] = visited[x][y]
                    if visited[nx][ny]:
                        swans.append((nx, ny))
                elif arr[nx][ny] == '.':
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y]
                        if visited[nx][ny]:
                            swans.append((nx, ny))
                    elif visited[nx][ny] != visited[x][y]:
                        flag = True
                        break
    if not flag:
        while swans:
            x, y = swans.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == '.' and visited[nx][ny] != 0 and visited[nx][ny] != visited[x][y]:
                        flag = True
                        break
    if flag:
        break
    water = new_water

print(ans)


