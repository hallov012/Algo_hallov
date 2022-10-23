import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pins = []
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y, d = map(int, input().split())
    pins.append([x-1, y-1, d-1])
    board[x-1][y-1].append(i)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
counter = {0: 1, 1: 0, 2: 3, 3: 2 }
ans = 1
flag = False
while ans <= 1000:
    for i in range(k):
        x, y, d = pins[i]
        if board[x][y][0] != i:
            continue
        nx = x + dx[d]
        ny = y + dy[d]
        if not 0 <= nx < n or not 0 <= ny < n or arr[nx][ny] == 2:
            nd = counter[d]
            pins[i][2] = nd
            nx = x + dx[nd]
            ny = y + dy[nd]
            if not 0 <= nx < n or not 0 <= ny < n or arr[nx][ny] == 2:
                continue
        move_pins = board[x][y]
        board[x][y] = []
        if arr[nx][ny] == 1:
            move_pins.reverse()
        for pin in move_pins:
            board[nx][ny].append(pin)
            pins[pin][0] = nx
            pins[pin][1] = ny
        if len(board[nx][ny]) >= 4:
            flag = True
            break
    if flag:
        break
    ans += 1
if ans > 1000:
    print(-1)
else:
    print(ans)