import sys
from collections import deque
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
cloud = [[0] * n for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
stack = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for x, y in stack:
    cloud[x][y] = 1

for d, s in move:
    d -= 1
    move_stack = []
    for x, y in stack:
        nx = ((x + dx[d]) * s) % n
        ny = ((y + dy[d]) * s) % n
        arr[nx][ny] += 1
        move_stack.append((nx, ny))

    for x, y in move_stack:
        cnt = 0
        for i in (-1, 1):
            for j in (-1, 1):
                nx = x + i
                ny = y + j
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                    cnt += 1
        arr[x][y] += cnt

    new_stack = []
    for x in range(n):
        for y in range(n):
            if (x, y) not in move_stack and arr[x][y] >= 2:
                arr[x][y] -= 2
                new_stack.append((x, y))
    stack = new_stack

ans = 0
for row in arr:
    ans += sum(row)
print(ans)
