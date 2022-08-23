import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
k = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

l = int(input())
command = []
for _ in range(l):
    t, d = map(str, input().split())
    command.append((int(t), d))
command.append((10001, ''))

x, y = 0, 0
snake = deque([(0, 0)])
dir = 0
time = 0

for i in range(len(command)):
    flag = True
    for _ in range(time, command[i][0]):
        time += 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake:
            # 사과가 있을 때
            if arr[nx][ny]:
                arr[nx][ny] = 0
            else:
                snake.popleft()
            snake.append((nx, ny))
            x, y = nx, ny
        else:
            flag = False
            break

    if not flag:
        break
    if command[i][1] == 'L':
        dir -= 1
        if dir == -1:
            dir = 3
    else:
        dir += 1
        if dir == 4:
            dir = 0

print(time)






