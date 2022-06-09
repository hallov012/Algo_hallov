import sys
from collections import deque

sys.stdin = open('input.txt')

def bfs():
    que = deque([(0, 0)])
    air_visited = [[0] * m for _ in range(n)]
    air_visited[0][0] = 1
    data[0][0] = -1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not air_visited[nx][ny]:
                if data[nx][ny] == 0 or data[nx][ny] == -1:
                    data[nx][ny] = -1
                    air_visited[nx][ny] = 1
                    que.append((nx, ny))
    return

def is_done():
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                return False
    return True

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

while not is_done():
    bfs()
    check = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == -1:
                        cnt += 1
                if cnt >= 2:
                    check.append((i, j))
    for x, y in check:
        data[x][y] = 0
    ans += 1

print(ans)