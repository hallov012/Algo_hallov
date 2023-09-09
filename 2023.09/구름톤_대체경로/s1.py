import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

n, m, s, e = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for t in range(1, n+1):
    if t == s or t == e:
        print(-1)
        continue
    visited = [0] * (n+1)
    que = deque([s])
    visited[s] = 1
    while que:
        x = que.popleft()
        for y in g[x]:
            if y != t and not visited[y]:
                visited[y] = visited[x] + 1
                que.append(y)
    if visited[e]:
        print(visited[e])
    else:
        print(-1)
