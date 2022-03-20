import sys
from collections import deque
sys.stdin = open('input.txt')

def counter(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 3
    else:
        return 2

T = int(input())

for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    # [상 하 좌 우] 상-하, 좌-우 는 연결되어 있어야한다?
    pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1],
            [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 1
    que = deque([[r, c]])
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    while que:
        x, y = que.popleft()
        here_pipe = pipe[data[x][y]]
        for i in range(4):
            if here_pipe[i]:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if data[nx][ny] != 0 and not visited[nx][ny]:
                        j = counter(i)
                        next_pipe = pipe[data[nx][ny]]
                        if next_pipe[j]:
                            visited[nx][ny] = visited[x][y] + 1
                            que.append([nx, ny])
                            if visited[nx][ny] <= l:
                                ans += 1
    print(f'#{tc} {ans}')
