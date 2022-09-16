import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

cnt = [0]
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    que = deque([i])
    while que:
        x = que.popleft()
        for y in g[x]:
            if not visited[y]:
                visited[y] = 1
                que.append(y)
    cnt.append(sum(visited))

max_cnt = 0
ans = []
for i in range(1, n+1):
    if cnt[i] > max_cnt:
        ans = [i]
        max_cnt = cnt[i]
    elif cnt[i] == max_cnt:
        ans.append(i)
print(*ans)