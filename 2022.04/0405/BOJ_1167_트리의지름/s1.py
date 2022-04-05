import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dfs(node, cnt):
    global ans, max_node
    if ans < cnt:
        ans = cnt
        max_node = node
    for e, d in g[node]:
        if not visited[e]:
            visited[e] = 1
            dfs(e, cnt+d)
            visited[e] = 0

input = sys.stdin.readline

V = int(input())
g = defaultdict(list)
for _ in range(V):
    data = list(map(int, input().split()))
    start = data[0]
    for i in range(1, len(data)-1, 2):
        e, d = data[i], data[i+1]
        g[start].append((e, d))

visited = [0] * (V+1)
ans = 0
max_node = 0

# 트리의 지름: 임의의 노드 x에서 dfs/bfs를 통해 가장 먼 노드 y를 구한 후 dfs/bfs를 한번 더 진행
visited[1] = 1
dfs(1, 0)
visited[1] = 0
visited[max_node] = 1
dfs(max_node, 0)

print(ans)