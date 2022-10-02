import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = []
me = [0, 0]
mad_lst = []

for i in range(r):
    row = list(input().strip())
    arr.append(row)
    for j in range(c):
        if arr[i][j] == 'I':
            me = [i, j]
        elif arr[i][j] == 'R':
            mad_lst.append([i, j])

move_lst = input()
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
# 종수의 위치: -1, 나머지는 1부터
time = 0
while time < len(move_lst):
    # 종수 이동
    me_nx = me[0] + dx[int(move_lst[time])]
    me_ny = me[1] + dy[int(move_lst[time])]
    if arr[me_nx][me_ny] == '.':
        arr[me[0]][me[1]] = '.'
        arr[me_nx][me_ny] = 'I'
        me = [me_nx, me_ny]
    else:
        print(f"kraj {time+1}")
    time += 1


