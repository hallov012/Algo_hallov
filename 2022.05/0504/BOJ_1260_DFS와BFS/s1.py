import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(x):
    dfs_visited[x] = 1
    dfs_ans.append(x)
    for i in range(1, n+1):
        if g[x][i] and not dfs_visited[i]:
            dfs(i)

input = sys.stdin.readline

n, m, v = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] += 1
    g[b][a] += 1
dfs_visited = [0] * (n+1)
dfs_ans = []
dfs(v)
print(*dfs_ans)

bfs_visited = [0] * (n+1)
bfs_ans = [v]
bfs_visited[v] = 1
que = deque([v])
while que:
    v = que.popleft()
    for i in range(1, n+1):
        if g[v][i] and not bfs_visited[i]:
            bfs_visited[i] = 1
            bfs_ans.append(i)
            que.append(i)
print(*bfs_ans)
