import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    sx, sy, ex, ey = 0, 0, n-1, n-1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    inf = 987654321
    dist = [[inf] * n for _ in range(n)]
    dist[sx][sy] = 0
    que = deque([(sx, sy)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                diff = 0
                if data[nx][ny] > data[x][y]:
                    diff = data[nx][ny] - data[x][y]
                if dist[nx][ny] > dist[x][y] + diff + 1:
                    dist[nx][ny] = dist[x][y] + diff + 1
                    que.append((nx, ny))
    print(f'#{tc} {dist[ex][ey]}')
