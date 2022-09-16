import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
island = [[0] * n for _ in range(n)]
num = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if arr[i][j] and not island[i][j]:
            island[i][j] = num
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] and not island[nx][ny]:
                            island[nx][ny] = num
                            que.append((nx, ny))
            num += 1

ans = sys.maxsize
for number in range(1, num-1):
    que =

