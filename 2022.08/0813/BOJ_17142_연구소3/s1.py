import sys
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    visited = [[0] * n for _ in range(n)]
    for x, y in que:
        visited[x][y] = 1
    time, cnt = 0, len(virus)
    while que:
        if n ** 2 == cnt + wall:
            return time
        k = len(que)
        for _ in range(k):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and arr[nx][ny] != 1:
                        visited[nx][ny] = 1
                        que.append((nx, ny))
                        if arr[nx][ny] == 0:
                            cnt += 1
        time += 1
    return -1

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
virus, wall = [], 0
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if line[j] == 2:
            virus.append((i, j))
        elif line[j] == 1:
            wall += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cases = list(combinations(virus, m))
ans = sys.maxsize
for case in cases:
    que = deque(list(case))
    temp = bfs()
    if temp != -1:
        ans = min(ans, temp)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
