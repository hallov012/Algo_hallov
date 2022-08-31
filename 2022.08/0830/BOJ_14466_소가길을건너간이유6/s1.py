import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k, r = map(int, input().split())
g = [[[] for _ in range(n)] for _ in range(n)]
cows = []
for _ in range(r):
    x1, y1, x2, y2 = map(int, input().split())
    g[x1-1][y1-1].append((x2-1, y2-1))
    g[x2-1][y2-1].append((x1-1, y1-1))
for _ in range(k):
    x, y = map(int, input().split())
    cows.append((x-1, y-1))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
for i in range(k):
    a, b = cows[i][0], cows[i][1]
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    que = deque([(a, b)])
    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and not (nx, ny) in g[x][y]:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
    for j in range(i+1, k):
        p, q = cows[j][0], cows[j][1]
        if not visited[p][q]:
            ans += 1

print(ans)

