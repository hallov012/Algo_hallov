import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    cores = []
    connected = 0
    connected_lst = []
    for i in range(n):
        for j in range(n):
            if data[i][j]:
                if i in [0, n] or j in [0, n]:
                    connected += 1
                    connected_lst.append([i, j])
                cores.append([i, j])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [(0, 0, 0, data)]
    ans = n * n
    while stack:
        core_idx, core_cnt, length, new_board = stack.pop()
        if core_idx == len(cores):
            if core_cnt > connected:
                connected = core_cnt
                ans = length
            elif core_cnt == connected:
                if ans > length:
                    ans = length
        elif core_cnt + (len(cores) - core_idx) >= connected:
            if cores[core_idx] not in connected_lst:
                for i in range(4):
                    now_board = [row[:] for row in new_board]
                    check = True
                    changes = []
                    x, y = cores[core_idx][0], cores[core_idx][1]
                    while 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if now_board[nx][ny]:
                            check = False
                            break
                        else:
                            changes.append([nx, ny])
                            x, y = nx, ny
                    if check:
                        for change in changes:
                            now_board[change[0]][change[1]] = 1
                        stack.append((core_idx+1, core_cnt+1, length+len(changes), now_board))
                    else:
                        stack.append((core_idx+1, core_cnt, length, new_board))
            else:
                stack.append((core_idx+1, core_cnt+1, length, new_board))
    print(f'#{tc} {ans}')



