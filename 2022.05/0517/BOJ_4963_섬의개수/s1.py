import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] and not visited[i][j]:
                ans += 1
                visited[i][j] = 1
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    for d in range(8):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < h and 0 <= ny < w:
                            if data[nx][ny] and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                que.append((nx, ny))
    print(ans)
