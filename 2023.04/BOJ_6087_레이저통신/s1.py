import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

w, h = map(int, input().split())
laser = []
visited = [[sys.maxsize] * w for _ in range(h)]
for i in range(h):
    line = list(input())
    for j in range(w):
        if line[j] == 'C':
            laser.append((i, j))
        elif line[j] == '*':
            visited[i][j] = -1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start, end = laser[0], laser[1]
visited[start[0]][start[1]] = 0
que = deque([(start[0], start[1])])
while que:
    x, y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if (nx, ny) == end:
                print(visited[x][y])
                exit()
            if not (0 <= nx < h and 0 <= ny < w):
                break
            if visited[nx][ny] == -1:
                break
            if visited[nx][ny] < visited[x][y] + 1:
                break
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))
            nx += dx[i]
            ny += dy[i]
