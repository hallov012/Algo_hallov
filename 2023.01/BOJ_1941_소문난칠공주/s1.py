import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(idx):
    a = idx // n
    b = idx % n
    visited = [[0] * n for _ in range(n)]
    visited[a][b] = 1
    cnt = 1
    que = deque([(a, b)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and (nx*5 + ny) in p:
                    visited[nx][ny] = 1
                    cnt += 1
                    que.append((nx, ny))
    return cnt

def dfs(cnt, idx, yn):
    global ans
    if yn >= 4 or 25-idx < 7-cnt:
        return
    if cnt == 7:
        connect_cnt = bfs(p[0])
        if connect_cnt == 7:
            ans += 1
        return
    x = idx // n
    y = idx % n
    p.append(idx)
    if arr[x][y] == 'Y':
        dfs(cnt+1, idx+1, yn+1)
    else:
        dfs(cnt+1, idx+1, yn)
    p.pop()
    dfs(cnt, idx+1, yn)

input = sys.stdin.readline

n = 5
arr = [input().rstrip() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
p = []
ans = 0
dfs(0, 0, 0)
print(ans)