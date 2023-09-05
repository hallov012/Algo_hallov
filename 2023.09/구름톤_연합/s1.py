import sys
from collections import deque
sys.stdin = open('input.txt')

n, m = map(int, input().split())
g = [[False] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = True

visited = [False] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        visited[i] = True
        que = deque([i])
        while que:
            x = que.popleft()
            for y in range(1, n+1):
                if g[x][y] and g[y][x] and not visited[y]:
                    visited[y] = True
                    que.append(y)

print(cnt)