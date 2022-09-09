import sys
sys.stdin = open('input.txt')

def dfs(now, cnt, cost):
    global ans
    if cnt == n:
        ans = min(ans, cost)
        return
    if cost >= ans:
        return
    for next in range(n):
        if not visited[next]:
            visited[next] = 1
            dfs(next, cnt+1, cost+dist[now][next])
            visited[next] = 0

input = sys.stdin.readline

n, k = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]
for t in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][t] + dist[t][j])

visited = [0] * n
visited[k] = 1
ans = sys.maxsize
dfs(k, 1, 0)
print(ans)

