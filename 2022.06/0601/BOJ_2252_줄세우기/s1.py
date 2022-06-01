import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
que = deque()
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if not in_degree[i]:
        que.append(i)

while que:
    v = que.popleft()
    ans.append(v)
    for w in g[v]:
        in_degree[w] -= 1
        if not in_degree[w]:
            que.append(w)

print(*ans)

