import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
w_start = 'WBWBWBWB'
b_start = 'BWBWBWBW'

board = [input() for _ in range(n)]
ans = 8 ** 2
for i in range(n - 8 + 1):
    for j in range(m - 8 + 1):
        cnt_1, cnt_2 = 0, 0
        new_board = [''] * 8
        for a in range(8):
            for b in range(8):
                new_board[a] += board[i+a][j+b]
        for x in range(8):
            if not x % 2:
                if new_board[x] == w_start:
                    pass
                else:
                    for y in range(8):
                        if new_board[x][y] != w_start[y]:
                            cnt_1 += 1
            else:
                if new_board[x] == b_start:
                    pass
                else:
                    for y in range(8):
                        if new_board[x][y] != b_start[y]:
                            cnt_1 += 1
        for x in range(8):
            if not x % 2:
                if new_board[x] == b_start:
                    pass
                else:
                    for y in range(8):
                        if new_board[x][y] != b_start[y]:
                            cnt_2 += 1
            else:
                if new_board[x] == w_start:
                    pass
                else:
                    for y in range(8):
                        if new_board[x][y] != w_start[y]:
                            cnt_2 += 1
        ans = min([ans, cnt_1, cnt_2])
print(ans)