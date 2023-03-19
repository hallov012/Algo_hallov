import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visited = [[0] * n for _ in range(n)]
visited[x1][y1] = 1
que = deque([(x1, y1)])
while que:
    x, y = que.popleft()
    if x == x2 and y == y2:
        print(visited[x2][y2]-1)
        break
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))
else:
    print(-1)