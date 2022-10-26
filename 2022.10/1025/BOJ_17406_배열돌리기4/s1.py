import sys, copy
from collections import deque
sys.stdin = open('input.txt')

def rotate(que):
    copy_arr = copy.deepcopy(arr)
    while que:
        x, y, s = que.popleft()
        lx, ly, rx, ry = x-s, y-s, x+s, y+s
        while True:
            if lx >= rx or ly >= ry:
                break
            d = 0
            x, y, before = lx, ly, copy_arr[lx][ly]
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if lx <= nx <= rx and ly <= ny <= ry:
                    temp = copy_arr[nx][ny]
                    copy_arr[nx][ny] = before
                    before = temp
                    x, y = nx, ny
                    if x == lx and y == ly:
                        lx += 1
                        ly += 1
                        rx -= 1
                        ry -= 1
                        break
                else:
                    d += 1
    min_sum = sys.maxsize
    for row in copy_arr:
        min_sum = min(min_sum, sum(row))
    return min_sum

def dfs(cnt):
    global ans
    if cnt == k:
        copy_que = copy.deepcopy(que)
        ans = min(ans, rotate(copy_que))
    for i in range(k):
        if not visited[i]:
            visited[i] = 1
            que.append(commands[i])
            dfs(cnt+1)
            que.pop()
            visited[i] = 0

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
commands = []
for _ in range(k):
    r, c, s = map(int, input().split())
    commands.append((r-1, c-1, s))
# 우 하 좌 상 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [0] * k
ans = sys.maxsize
que = deque()
dfs(0)
print(ans)