import sys
sys.stdin = open('input.txt')

def dfs(i, cnt):
    global ans
    ans = max(ans, cnt)
    for j in range(1, n+1):
        if not visited[j] and g[i][j]:
            visited[j] = 1
            dfs(j, cnt + 1)
            visited[j] = 0

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    if not m:
        print(f'#{tc} 1')
        continue
    g = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
        g[b][a] = 1
    visited = [0] * (n+1)
    ans = 0
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print(f'#{tc} {ans}')