import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt')

def dfs(node, cnt):
    global ans, max_node
    if ans < cnt:
        ans = cnt
        max_node = node
    for e, w in g[node]:
        if not visited[e]:
            visited[e] = 1
            dfs(e, cnt+w)
            visited[e] = 0



input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for _ in range(n-1):
    s, e, w = map(int, input().split())
    g[s].append((e, w))
    g[e].append((s, w))

inf = 987654321
visited = [0] * (n+1)
ans = 0
max_node = 0

visited[1] = 1
dfs(1, 0)
visited[1] = 0
visited[max_node] = 1
dfs(max_node, 0)
print(ans)
