import sys
sys.stdin = open('input.txt')

def dfs(x, y, val, cnt):
    global ans
    if cnt == n:
        ans += val
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m+1 and 0 <= ny < m+1:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, val*(p[i]/100), cnt+1)
                visited[nx][ny] = 0

data = list(map(int, input().split()))
n = data[0]
p = data[1:]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
m = 2*n
visited = [[0] * (m+1) for _ in range(m+1)]
visited[n][n] = 1
ans = 0
dfs(n, n, 1, 0)
print(ans)