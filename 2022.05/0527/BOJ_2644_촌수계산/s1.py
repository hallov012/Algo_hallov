import sys
from collections import defaultdict
sys.setrecursionlimit(300000)

sys.stdin = open('input.txt')

def dfs(v):
    for w in g[v]:
        if not visited[w]:
            visited[w] = visited[v] + 1
            dfs(w)

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
g = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

visited = [0] * (n+1)
visited[a] = 1
dfs(a)
if visited[b] > 1:
    print(visited[b] - 1)
else:
    print(-1)

