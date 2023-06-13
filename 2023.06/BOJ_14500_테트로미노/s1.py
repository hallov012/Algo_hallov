import sys
sys.stdin = open('input.txt')

def dfs(x, y, cnt, val):
    global ans
    if ans >= val + max_val * (3 - cnt):
        return
    if cnt == 3:
        ans = max(ans, val)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 1:
                visited[nx][ny] = 1
                dfs(x, y, cnt+1, val + arr[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, val + arr[nx][ny])
            visited[nx][ny] = 0

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
max_val = max(map(max, arr))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0

print(ans)
