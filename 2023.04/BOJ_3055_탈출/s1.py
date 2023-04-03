import sys
from collections import deque
sys.stdin = open('input.txt')

def water_move():
    new_water = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and (arr[nx][ny] == '.' or arr[nx][ny] == 'S'):
                arr[nx][ny] = '*'
                new_water.append((nx, ny))
    return new_water


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
print(arr)
water = deque()
que = deque()
sx, sy = 0, 0
ex, ey = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(r):
    for j in range(c):
        if arr[i][j] == '*':
            water.append((i, j))
        elif arr[i][j] == 'S':
            sx, sy = i, j
        else:
            ex, ey = i, j
            arr[i][j] = '*'

while True:
    water = water_move()
