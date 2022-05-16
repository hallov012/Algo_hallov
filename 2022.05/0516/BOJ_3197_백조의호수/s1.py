import sys
from collections import deque
sys.stdin = open('input.txt')

def first_swan_move(swans):
    global swans_que
    new_swans = deque()
    while swans:
        x, y, number, check = swans.popleft()
        flag = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if data[nx][ny] == 'X' and not flag:
                    new_swans.append((x, y, number, False))
                    flag = True
                elif data[nx][ny] != 'X':
                    if not visited[nx][ny]:
                        visited[nx][ny] = number
                        swans.append((nx, ny, number, False))
                    elif visited[nx][ny] != number:
                        return True
    swans_que = new_swans
    return False

def swan_break(swans):
    global swans_que
    new_swans = deque()
    while swans:
        x, y, number, check = swans_que.popleft()
        flag = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if data[nx][ny] == 'X':
                    if check and not flag:
                        new_swans.append((x, y, number, False))
                        flag = True
                    elif not check and not flag:
                        data[nx][ny] = '.'
                        visited[nx][ny] = number
                        swans.append((nx, ny, number, True))
                        new_swans.append((x, y, number, False))
                        flag = True
                elif data[nx][ny] == '.':
                    if check:
                        if not visited[nx][ny]:
                            visited[nx][ny] = number
                            swans.append((nx, ny, number, check))
                        elif visited[nx][ny] != number:
                            return True

    swans_que = new_swans
    return False

input = sys.stdin.readline

r, c = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data = []
swans_que = deque()
swan = 1
visited = [[0] * c for _ in range(r)]

for i in range(r):
    line = list(map(str, input().strip()))
    for j in range(c):
        if line[j] == 'L':
            swans_que.append((i, j, swan, False))
            visited[i][j] = swan
            swan += 1
            line[j] = '.'
    data.append(line)

ans = 0
if first_swan_move(swans_que):
    print(ans)
else:
    ans += 1
    while swan_break(swans_que) == False:
        ans += 1
    print(ans)

