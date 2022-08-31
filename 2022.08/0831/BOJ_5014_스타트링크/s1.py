import sys
from collections import deque
sys.stdin = open('input.txt')

f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)
visited[s] = 1
que = deque([s])
while que:
    now = que.popleft()
    if now+u <= f and not visited[now+u]:
        visited[now+u] = visited[now] + 1
        que.append(now+u)
    if now-d > 0 and not visited[now-d]:
        visited[now-d] = visited[now] + 1
        que.append(now-d)
if visited[g]:
    print(visited[g]-1)
else:
    print("use the stairs")
