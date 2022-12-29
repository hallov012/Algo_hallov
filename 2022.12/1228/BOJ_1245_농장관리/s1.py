import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(a, b):
    global ans
    ans += 1
    que = deque([(a, b)])
    check = [[0] * m for _ in range(n)]
    check[a][b] = 1
    temp = arr[a][b]
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not check[nx][ny]:
                if arr[nx][ny] > temp:
                    ans -= 1
                    return False
                elif arr[nx][ny] == temp:
                    if visited[nx][ny]:
                        ans -= 1
                        return True
                    check[nx][ny] = 1
                    que.append((nx, ny))
    return True

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            if bfs(i, j):
                visited[i][j] = 1

print(ans)


