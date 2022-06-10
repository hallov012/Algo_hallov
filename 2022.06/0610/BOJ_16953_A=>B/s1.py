import sys
from collections import deque
sys.stdin = open('input.txt')

a, b = map(int, input().split())
que = deque([(a, 1)])
ans = -1
while que:
    n, cnt = que.popleft()
    if n == b:
        ans = cnt
        break
    if n*2 <= b:
        que.append((n*2, cnt+1))
    if 10*n + 1 <= b:
        que.append((10*n+1, cnt+1))

print(ans)

