import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

# test
input = sys.stdin.readline

n, m = map(int, input().split())
degree = [0] * (n+1)
g = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    degree[b] += 1

que = deque()
for i in range(1, n+1):
    if not degree[i]:
        que.append((i, 1))

ans = [0] * n
while que:
    x, cnt = que.popleft()
    for y in g[x]:
        degree[y] -= 1
        if not degree[y]:
            que.append((y, cnt+1))
    ans[x-1] = cnt

print(*ans)

