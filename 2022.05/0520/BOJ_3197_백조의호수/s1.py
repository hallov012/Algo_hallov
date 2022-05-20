import sys
from collections import deque
sys.stdin = open('input.txt')

def melt_ice():
    while water_que:
        x, y = water_que.popleft()
        if arr[x][y] == 'X':
            arr[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not water[nx][ny]:
                    water[nx][ny] = 1
                    if arr[nx][ny] == 'X':
                        new_water_que.append((nx, ny))
                    else:
                        water_que.append((nx, ny))

def bfs():
    while que:
        x, y = que.popleft()
        if x == swans[1][0] and y == swans[1][1]:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if arr[nx][ny] == '.':
                        que.append((nx, ny))
                    else:
                        new_que.append((nx, ny))
    return False


input = sys.stdin.readline

r, c = map(int, input().split())
water = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
que, new_que = deque(), deque()
water_que, new_water_que = deque(), deque()
arr, swans = [], []
for i in range(r):
    line = list(input().strip())
    for j in range(c):
        if line[j] == 'L':
            line[j] = '.'
            swans.append((i, j))
            water_que.append((i, j))
            water[i][j] = 1
        elif line[j] == '.':
            water[i][j] = 1
            water_que.append((i, j))
    arr.append(line)

que.append(swans[0])
visited[swans[0][0]][swans[0][1]] = 1
ans = 0

while True:
    melt_ice()
    if bfs():
        print(ans)
        break
    que = new_que
    water_que = new_water_que
    new_que, new_water_que = deque(), deque()
    ans += 1