import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
m = 500001
visited = [[-1, -1] for _ in range(m)]
ans = 0
que = deque([(n, 0)])
visited[n][0] = 0

time = 0
ans = -1
while k < m:
    k_flag = time % 2
    if visited[k][k_flag] != -1:
        if visited[k][k_flag] <= time:
            ans = time
            break
    time += 1
    k += time

    new_que = []
    while que:
        now, cnt = que.popleft()
        for next in (now-1, now+1, 2*now):
            flag = (cnt+1) % 2
            if 0 <= next < m and visited[next][flag] == -1:
                visited[next][flag] = cnt + 1
                new_que.append((next, cnt+1))

    que = deque(new_que)

print(ans)