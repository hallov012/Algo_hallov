import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    ans = 0
    n = int(input())
    que = deque([n])
    while que:
        m = que.popleft()
        if not m:
            ans += 1
        else:
            if m >= 3:
                que.append(m-3)
            if m >= 2:
                que.append(m-2)
            if m >= 1:
                que.append(m-1)
    print(ans)
