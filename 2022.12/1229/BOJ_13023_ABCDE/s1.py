import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    if cnt == 5:
        print(1)
        exit()
    for i in g[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

input = sys.stdin.readline

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
visited = [0] * n

for i in range(n):
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0

print(0)