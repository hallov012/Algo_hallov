import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[100] * m for _ in range(n)]
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if data[i][j] == 3:
                end = [i, j]
                break
    visited[n-1][0] = 0
    que = deque([(n-1, 0)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            if i in [0, 1]:  # 위, 아래로 움직이는 경우
                now_lv = 1
                flag = False
                nx = x + dx[i]
                ny = y + dy[i]
                while 0 <= nx < n and 0 <= ny < m:
                    if data[nx][ny] == 1 or data[nx][ny] == 3:
                        flag = True
                        break
                    nx += dx[i]
                    ny += dy[i]
                    now_lv += 1
                if flag:
                    lv = max(visited[x][y], now_lv)
                    if lv < visited[nx][ny]:
                        visited[nx][ny] = lv
                        que.append((nx, ny))
            else:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if data[nx][ny] == 1 or data[nx][ny] == 3:
                        if visited[x][y] < visited[nx][ny]:
                            visited[nx][ny] = visited[x][y]
                            que.append((nx, ny))
    ans = visited[end[0]][end[1]]
    print(f'#{tc} {ans}')

