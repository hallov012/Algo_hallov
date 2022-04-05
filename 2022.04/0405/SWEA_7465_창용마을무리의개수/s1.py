import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)
    visited = [0] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            ans += 1
            que = deque([i])
            while que:
                v = que.popleft()
                for w in g[v]:
                    if not visited[w]:
                        visited[w] = 1
                        que.append(w)
    print(f'#{tc} {ans}')
