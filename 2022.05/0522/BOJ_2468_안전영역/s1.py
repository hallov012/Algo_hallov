import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = []
min_h = 100
max_h = 0
for _ in range(n):
    line = list(map(int, input().split()))
    min_h = min(min_h, min(line))
    max_h = max(max_h, max(line))
    arr.append(line)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
for k in range(min_h, max_h+1):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= k and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] >= k and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
    ans = max(ans, cnt)
print(ans)
