import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1
que = deque([(0, 0)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d = sys.maxsize
ans = sys.maxsize
while que:
    x, y = que.popleft()
    if arr[x][y] == 2:
        d = (visited[x][y]-1) + (n-1-x) + (m-1-y)
    if x == n-1 and y == m-1:
        ans = min(visited[x][y] - 1, d)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
else:
    ans = d
if ans > t:
    print("Fail")
else:
    print(ans)

