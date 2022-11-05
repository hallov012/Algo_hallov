import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr, wall = [], []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(m):
        if row[j]:
            wall.append((i, j))
h, w, sx, sy, fx, fy = map(int, input().split())
visited = [[0] * m for _ in range(n)]
visited[sx-1][sy-1] = 1
que = deque([(sx-1, sy-1)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que:
    x, y = que.popleft()
    if x == fx-1 and y == fy-1:
        print(visited[x][y]-1)
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n-h+1 and 0 <= ny < m-w+1 and not visited[nx][ny]:
            for wx, wy in wall:
                if nx <= wx < nx+h and ny <= wy < ny+w:
                    break
            else:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
else:
    print(-1)
