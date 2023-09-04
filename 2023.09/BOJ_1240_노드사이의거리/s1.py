import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(now, end):
    global ans
    if now == end:
        ans = min(ans, visited[now])
        return
    for next, d in g[now]:
        if visited[next] > visited[now] + d:
            visited[next] = visited[now] + d
            dfs(next, end)

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    ans = sys.maxsize
    visited = [sys.maxsize] * (n + 1)
    visited[a] = 0
    dfs(a, b)
    print(ans)