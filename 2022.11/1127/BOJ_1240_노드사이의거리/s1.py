import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start, end):
    que = deque([(start, 0)])
    visited = [0] * (n+1)
    visited[start] = 1
    while que:
        now, d = que.popleft()
        if now == end:
            return d
        for next, c in g[now]:
            if not visited[next]:
                visited[next] = 1
                que.append((next, d+c))

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))

