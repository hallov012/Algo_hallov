import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
num = 100000 * 2
visited = [0] * (num + 1)
visited[n] = 1
que = deque([[n, 0]])
while que:
    now, cnt = que.popleft()
    if now == k:
        print(cnt)
        break
    if now * 2 <= num and not visited[now*2]:
        visited[now*2] = 1
        que.appendleft([now*2, cnt])
    if now-1 >= 0 and not visited[now-1]:
        visited[now-1] = 1
        que.append([now-1, cnt+1])
    if now+1 <= num and not visited[now+1]:
        visited[now+1] = 1
        que.append([now+1, cnt+1])
