import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
que = deque()
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(m):
        if row[j]:
            que.append((i, j))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0
while que:
    x, y = que.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[nx][ny]:
                que.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
                ans = max(ans, arr[nx][ny])
print(ans-1)