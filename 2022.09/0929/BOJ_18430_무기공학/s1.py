import sys
sys.stdin = open('input.txt')

def dfs(i, j, cnt):
    global ans
    if j == m:
        i += 1
        j = 0
    if i == n:
        ans = max(ans, cnt)
        return
    if not visited[i][j]:
        for d in range(4):
            d1, d2 = d_dict[d]
            x1, y1 = i + dx[d1], j + dy[d1]
            x2, y2 = i + dx[d2], j + dy[d2]
            if 0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < m and 0 <= y2 < m:
                if not visited[x1][y1] and not visited[x2][y2]:
                    visited[i][j] = visited[x1][y1] = visited[x2][y2] = 1
                    dfs(i, j+1, cnt + arr[i][j] * 2 + arr[x1][y1] + arr[x2][y2])
                    visited[i][j] = visited[x1][y1] = visited[x2][y2] = 0
    dfs(i, j+1, cnt)

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
d_dict = {0: [0, 2], 1: [1, 2], 2: [0, 3], 3: [1, 3]}
visited = [[0] * m for _ in range(n)]
ans = 0
dfs(0, 0, 0)
print(ans)