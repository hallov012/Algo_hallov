import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [0] * (n+1)
ans = 0
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        que = deque([i])
        while que:
            v = que.popleft()
            for w in g[v]:
                if not visited[w]:
                    visited[w] = 1
                    que.append(w)
print(ans)