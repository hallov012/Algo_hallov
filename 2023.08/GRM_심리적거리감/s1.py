import sys
from collections import deque
sys.stdin = open('input.txt')

n, m, k = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    g[s].append(e)

dist = [-1] * (n+1)
dist[k] = 0
que = deque([k])
while que:
    x = que.popleft()
    for y in g[x]:
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            que.append(y)

max_num = 0
ans = -1
for i in range(n, 0, -1):
    if i == k or dist[i] == -1:
        continue
    tmp = dist[i] + abs(k-i)
    if max_num < tmp:
        max_num = tmp
        ans = i

print(ans)
