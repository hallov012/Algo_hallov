import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = n * n
    visited[0][0] = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque([[0, 0]])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    que.append([nx, ny])
                elif visited[x][y] + arr[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    que.append([nx, ny])
    ans = visited[n-1][n-1] - 1
    print(f'#{tc} {ans}')