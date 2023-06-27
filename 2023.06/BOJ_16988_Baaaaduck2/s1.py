import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def find_position(cnt, temp, idx):
    if cnt == 2:
        cases.append(temp.copy())
        return
    for i in range(idx+1, len(empty)):
        temp.append(empty[i])
        find_position(cnt+1, temp, i)
        temp.pop()

def bfs(x, y, visited):
    que = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    flag = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                   flag = False
                elif arr[nx][ny] == 2:
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny))
    if flag:
        return cnt
    else:
        return 0

def play(position):
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for x, y in position:
        arr[x][y] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 and not visited[i][j]:
                temp = bfs(i, j, visited)
                if temp:
                    cnt += temp
    for x, y in position:
        arr[x][y] = 0
    return cnt

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
empty = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(m):
        if not arr[i][j]:
            empty.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0

cases = []
find_position(0, [], -1)

for case in cases:
    ans = max(ans, play(case))

print(ans)
