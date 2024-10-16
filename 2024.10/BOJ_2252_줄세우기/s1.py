import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
in_cnt = [0] * (n+1)
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    in_cnt[b] += 1
    g[a].append(b)

q = deque()
for i in range(1, n+1):
    if not in_cnt[i]:
        q.append(i)

ans = []
while q:
    x = q.popleft()
    ans.append(x)
    for y in g[x]:
        in_cnt[y] -= 1
        if not in_cnt[y]:
            q.append(y)

print(*ans)