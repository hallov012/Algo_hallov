import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
m = 100001
visited = [0] * m
visited[n] = 1
path = [0] * m
que = deque([n])
while que:
    now = que.popleft()
    if now == k:
        break
    for next in (now-1, now+1, 2*now):
        if 0 <= next < m and not visited[next]:
            visited[next] = visited[now] + 1
            # 이전 경로를 path에 저장
            path[next] = now
            que.append(next)

print(visited[k] - 1)
ans = []
while k != n:
    ans.append(k)
    k = path[k]
ans.append(n)
print(*reversed(ans))
