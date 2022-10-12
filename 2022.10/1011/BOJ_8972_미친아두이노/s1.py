import sys
from collections import deque, defaultdict
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

move_lst = input().rstrip()
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
# 종수의 위치: -1, 나머지는 1부터
time = 0
whole_flag = True
while time < len(move_lst):
    time += 1
    # 종수 이동
    if int(move_lst[time-1]) != 5:
        me_nx = me[0] + dx[int(move_lst[time-1])]
        me_ny = me[1] + dy[int(move_lst[time-1])]
        if arr[me_nx][me_ny] == '.':
            arr[me[0]][me[1]] = '.'
            arr[me_nx][me_ny] = 'I'
            me = [me_nx, me_ny]
        else:
            whole_flag = False
            print(f"kraj {time}")
            break
    # 미친 아두이노 이동
    flag = True
    cnt = defaultdict(int)
    for x, y in mad_lst:
        temp = sys.maxsize
        dir = 0
        for i in range(1, 10):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if abs(me[0]-nx) + abs(me[1]-ny) < temp:
                    temp = abs(me[0]-nx) + abs(me[1]-ny)
                    dir = i
        if x + dx[dir] == me[0] and y + dy[dir] == me[1]:
            flag = False
            break
        else:
            cnt[(x+dx[dir], y+dy[dir])] += 1
            arr[x][y] = '.'
    if not flag:
        whole_flag = False
        print(f"kraj {time}")
        break
    new_mad = []
    for x, y in cnt.keys():
        if cnt[(x, y)] > 1:
            continue
        else:
            new_mad.append((x, y))
            arr[x][y] = 'R'
    mad_lst = new_mad[:]

if whole_flag:
    for row in arr:
        print("".join(row))