import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    board = [['X'] * n for _ in range(n)]
    games = [list(map(int, input().split())) for _ in range(m)]
    board[n//2-1][n//2-1] = board[n//2][n//2] = 'W'
    board[n//2][n//2-1] = board[n//2-1][n//2] = 'B'
    ans = [2, 2]
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    for game in games:
        if game[2] == 1: # 흑돌 놓기
            x, y = game[0]-1, game[1]-1
            board[x][y] = 'B'
            ans[0] += 1
            for i in range(8):
                changes = []
                while 1:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'W':
                            changes.append([nx, ny])
                            x, y = nx, ny
                        elif board[nx][ny] == 'B':
                            if len(changes) > 0:
                                for change in changes:
                                    board[change[0]][change[1]] = 'B'
                                ans[0] += len(changes)
                                ans[1] -= len(changes)
                            x, y = game[0] - 1, game[1] - 1
                            break
                        else:
                            x, y = game[0] - 1, game[1] - 1
                            break
                    else:
                        x, y = game[0] - 1, game[1] - 1
                        break
        if game[2] == 2: # 백돌 놓기
            x, y = game[0]-1, game[1]-1
            board[x][y] = 'W'
            ans[1] += 1
            for i in range(8):
                changes = []
                while 1:
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'B':
                            changes.append([nx, ny])
                            x, y = nx, ny
                        elif board[nx][ny] == 'W':
                            if len(changes) > 0:
                                for change in changes:
                                    board[change[0]][change[1]] = 'W'
                                ans[1] += len(changes)
                                ans[0] -= len(changes)
                            x, y = game[0] - 1, game[1] - 1
                            break
                        else:
                            x, y = game[0] - 1, game[1] - 1
                            break
                    else:
                        x, y = game[0] - 1, game[1] - 1
                        break
    print(f'#{tc} {ans[0]} {ans[1]}')