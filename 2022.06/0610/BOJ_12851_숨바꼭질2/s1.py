import sys
from collections import deque,defaultdict
sys.stdin = open('input.txt')

n, k = map(int, input().split())
visited = [0] * 100001
visited[n] = 1
que = deque([(n, 0)])
ans = defaultdict(int)
while que:
    now, cnt = que.popleft()
    visited[now] = 1
    if now == k:
        ans[cnt] += 1
    else:
        if now + 1 <= 100000 and not visited[now+1]:
            que.append((now+1, cnt+1))
        if 0 <= now - 1 and not visited[now-1]:
            que.append((now-1, cnt+1))
        if now * 2 <= 100000 and not visited[now*2]:
            que.append((now*2, cnt+1))

for key in ans.keys():
    print(key)
    print(ans[key])
    break

