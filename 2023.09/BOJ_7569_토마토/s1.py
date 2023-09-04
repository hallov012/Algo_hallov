import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

m, n, h = map(int, input().split())
boxs = []
not_ripe = 0
que = deque()
for k in range(h):
    box = []
    for i in range(n):
        line = list(map(int, input().split()))
        box.append(line)
        for j in range(m):
            if box[i][j] == 1:
                que.append((i, j, k))
            elif box[i][j] == 0:
                not_ripe += 1
    boxs.append(box)

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

if not_ripe == 0:
    print(0)
    exit()

ans = 0
while True:
    k = len(que)
    for _ in range(k):
        x, y, z = que.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if boxs[nz][nx][ny] == 0:
                    boxs[nz][nx][ny] = 1
                    not_ripe -= 1
                    que.append((nx, ny, nz))
    if que:
        ans += 1
    else:
        break

if not_ripe:
    print(-1)
else:
    print(ans)


