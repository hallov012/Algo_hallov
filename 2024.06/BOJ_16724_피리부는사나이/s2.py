import sys
sys.stdin = open('input.txt')

def dfs(x, y):
    global ans
    d = arr[x][y]
    nx = x + direct[d][0]
    ny = y + direct[d][1]

    if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            cycle.append((nx, ny))
            dfs(nx, ny)
        else:
            # 이미 지나간 자리라면 해당 cycle에 있는 사람이 모두 지나갈 수 있으므로 safeZone 설치
            if (nx, ny) in cycle:
                ans += 1

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
direct = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

visited = [[0] * m for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            cycle = [(i, j)]
            dfs(i, j)

print(ans)