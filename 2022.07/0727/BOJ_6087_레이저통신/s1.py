import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

w, h = map(int, input().split())
arr = []
laser = []
for i in range(h):
    line = list(input())
    arr.append(line)
    for j in range(w):
        if line[j] == 'C':
            laser.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
start, end = laser[0], laser[1]
visited = [[sys.maxsize] * w for _ in range(h)]
visited[start[0]][start[1]] = 0
que = deque([(start[0], start[1], 0, -1)])
while que:
    x, y, cnt, d = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if d != i:
                temp = cnt + 1
            else:
                temp = cnt
            if visited[nx][ny] >= temp and arr[nx][ny] != '*':
                visited[nx][ny] = temp
                que.append((nx, ny, temp, i))

print(visited[end[0]][end[1]]-1)

