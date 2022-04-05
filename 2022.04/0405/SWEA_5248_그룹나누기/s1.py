import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    g = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = temp[2*i], temp[2*i+1]
        g[a].append(b)
        g[b].append(a)
    visited = [0] * (n + 1)
    ans = 0
    for j in range(1, n+1):
        if not visited[j]:
            ans += 1
            visited[j] = 1
            que = deque([j])
            while que:
                v = que.popleft()
                for w in g[v]:
                    if not visited[w]:
                        visited[w] = 1
                        que.append(w)
    print(f'#{tc} {ans}')