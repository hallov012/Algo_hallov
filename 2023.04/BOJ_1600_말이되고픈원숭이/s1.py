import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
sx = [-2, -2, -1, -1, 1, 1, 2, 2]
sy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

que = deque([(0, 0, 0)])
while que:
    x, y, z = que.popleft()
    if x == h-1 and y == w-1:
        print(visited[x][y][z])
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if not arr[nx][ny] and not visited[nx][ny][z]:
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append((nx, ny, z))
    if z < k:
        for i in range(8):
            nx = x + sx[i]
            ny = y + sy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not arr[nx][ny] and not visited[nx][ny][z+1]:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    que.append((nx, ny, z+1))
else:
    print(-1)
