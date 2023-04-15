import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
que = deque([(1, 0)])
visited = [[0] * (n+1) for _ in range(n+1)]
visited[1][0] = 1
while que:
    s, c = que.popleft()
    if not visited[s][s]:
        visited[s][s] = visited[s][c] + 1
        que.append((s, s))
    if s+c <= n and not visited[s+c][c]:
        visited[s+c][c] = visited[s][c] + 1
        que.append((s+c, c))
    if s-1 >= 0 and not visited[s-1][c]:
        visited[s-1][c] = visited[s][c] + 1
        que.append((s-1, c))
ans = sys.maxsize

for i in range(n+1):
    if visited[n][i] and ans > visited[n][i]:
        ans = visited[n][i]
print(ans-1)