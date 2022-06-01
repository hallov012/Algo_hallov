import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 해당 지점까지 온 경우의 개수를 메모이제이션하며 dfs를 실행
def dfs(x, y):
    # 목적지에 도착했을 경우 1을 더해줌
    if x == m-1 and y == n-1:
        return 1
    # 한번도 방문을 하지 않았을 경우
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if data[nx][ny] < data[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]

input = sys.stdin.readline

m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dfs(0, 0)
print(visited[0][0])

