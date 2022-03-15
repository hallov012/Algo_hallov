import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    start, end = [], []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                end = [i, j]
    visited[start[0]][start[1]] = 1
    que = [start]
    while que:
        x, y = que.pop(0)
        if x == end[0] and y == end[1]:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not maze[nx][ny] or maze[nx][ny] == 3:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        que.append([nx, ny])
    if not visited[end[0]][end[1]]:
        ans = 0
    else:
        ans = visited[end[0]][end[1]] -2
    print(f'#{tc} {ans}')