import sys
from collections import deque
sys.stdin = open('input.txt')

def move(x, y, d):
    c = 0
    while arr[x+dx[d]][y+dy[d]] != '#' and arr[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        c += 1
    return x, y, c

def bfs():
    while que:
        ri, rj, bi, bj, cnt = que.popleft()
        if cnt > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, i)
            nbi, nbj, bc = move(bi, bj, i)
            if arr[nbi][nbj] != 'O':
                if arr[nri][nrj] == 'O':
                    print(cnt)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visited[nri][nrj][nbi][nbj]:
                    visited[nri][nrj][nbi][nbj] = 1
                    que.append((nri, nrj, nbi, nbj, cnt+1))
    print(-1)

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    row = list(input())
    arr.append(row)
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

que = deque([(rx, ry, bx, by, 1)])
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by] = 1

bfs()

