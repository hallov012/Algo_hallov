import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited[0][0][0] = 1
que = deque([[0, 0, 0]])
ans = -1
while que:
    x, y, check = que.popleft()
    if x == n-1 and y == m-1:
        ans = visited[x][y][check]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][check]:
            if not arr[nx][ny]:
                visited[nx][ny][check] = visited[x][y][check] + 1
                que.append([nx, ny, check])
            elif arr[nx][ny] and not check:
                visited[nx][ny][1] = visited[x][y][check] + 1
                que.append([nx, ny, 1])
print(ans)