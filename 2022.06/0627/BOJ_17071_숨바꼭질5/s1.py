"""
이전의 숨바꼭질 문제와는 다르게 한번 방문한 곳도 다시 방문할 수 있음
만약 15초에 10이라는 지점에 최초로 도착했다면 10=>11=>10 또는 10=>9=>10으로 이동해서
그 후 17, 19, 21,.. 모든 홀수시간에 10이라는 지점에 다시 도착할 수 있다
짝수도 마찬가지이므로 visited를  [[-1, -1] for _ in range(m)]으로 최초로 도달하는 짝수시간, 홀수 시간을 따로 저장한다
"""

import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
m = 500001
visited = [[-1, -1] for _ in range(m)]
ans = 0
que = deque([(n, 0)])
visited[n][0] = 0
while que:
    now, cnt = que.popleft()
    for next in (now-1, now+1, 2*now):
        flag = (cnt+1) % 2
        # 짝수 시간대에 도착한다면 visited[next][0]
        # 홀수 시간대에 도착한다면 visited[next][1]
        if 0 <= next < m and visited[next][flag] == -1:
            visited[next][flag] = cnt + 1
            que.append((next, cnt + 1))

time = 0
flag = 0
ans = -1
while k < m:
    if visited[k][flag] != -1:
        # 만약 동생이 해당 위치에 도착하는 순간이 flag시간 일 때,
        # 그 전에 같은 flag로 수빈이가 방문했었다면 그 곳에서 계속 반복하며 방문할 수 있기 때문에 만날 수 있음
        if visited[k][flag] <= time:
            ans = time
            break
    flag = 1 - flag
    time += 1
    k += time

print(ans)
