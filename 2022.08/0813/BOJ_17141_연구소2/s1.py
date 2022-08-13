import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def bfs():
    visited = [[0] * n for _ in range(n)]
    for x, y in que:
        visited[x][y] = 1
    time, cnt = -1, len(que)
    while que:
        k = len(que)
        for _ in range(k):
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and not arr[nx][ny] == 1:
                        visited[nx][ny] = 1
                        cnt += 1
                        que.append((nx, ny))
        time += 1
    return time, cnt

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
virus = []
wall = 0
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if line[j] == 2:
            virus.append((i, j))
            arr[i][j] = 0
        if line[j] == 1:
            wall += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = sys.maxsize
cases = list(combinations(virus, m))
for case in cases:
    que = deque(list(case))
    time, cnt = bfs()
    if n ** 2 == cnt + wall:
        ans = min(ans, time)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)



