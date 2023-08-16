import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

def divide_bfs(idx, a, b):
    que = deque([(a, b)])
    island[a][b] = idx
    island_idx[idx].append((a, b))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not island[nx][ny] and arr[nx][ny] == 1:
                island[nx][ny] = idx
                que.append((nx, ny))
                island_idx[idx].append((nx, ny))
    return

def find_bfs(idx):
    global ans
    visited = [[0] * n for _ in range(n)]
    que = deque()
    for a, b in island_idx[idx]:
        que.append((a, b))
        visited[a][b] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if island[nx][ny] and island[nx][ny] != idx:
                    ans = min(ans, visited[x][y]-1)
                if not visited[nx][ny] and not arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    return

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
island = [[0] * n for _ in range(n)]
island_idx = defaultdict(list)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if not island[i][j] and arr[i][j]:
            divide_bfs(cnt, i, j)
            cnt += 1

for i in range(1, cnt):
    find_bfs(i)

print(ans)




