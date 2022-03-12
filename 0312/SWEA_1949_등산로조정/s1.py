import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    max_h = 0
    max_lst = []
    for r in range(n):
        for c in range(n):
            if max_h < mountain[r][c]:
                max_h = mountain[r][c]
                max_lst = []
            if max_h == mountain[r][c]:
                max_lst.append([r, c])
    ans = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            for a in range(1, k+1):
                mountain[i][j] -= a
                if mountain[i][j] < 0:
                    mountain[i][j] += a
                    break
                for start in max_lst:
                    visited = [[0] * n for _ in range(n)]
                    que = deque([start])
                    visited[start[0]][start[1]] = 1
                    while que:
                        x, y = que.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                if mountain[x][y] > mountain[nx][ny]:
                                    que.append([nx, ny])
                                    visited[nx][ny] = visited[x][y] + 1
                    is_it_max = max([max(visited[l]) for l in range(n)])
                    ans = max(ans, is_it_max)
                mountain[i][j] += a
    print(f'#{tc} {ans}')


