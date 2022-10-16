import sys
from collections import deque
sys.stdin = open('input.txt')

a, b, c = map(int, input().split())
visited = [[0] * 1501 for _ in range(1501)]
total = a + b + c
if total % 3:
    print(0)
else:
    ans = 0
    que = deque([(a, b)])
    visited[a][b] = 1
    while que:
        a, b = que.popleft()
        c = total - a - b
        if a == b and b == c:
            ans = 1
            break
        for x, y in [(a, b), (b, c), (a, c)]:
            if x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            else:
                continue
            z = total - x - y
            a = min(min(x, y), z)
            b = max(max(x, y), z)
            if not visited[a][b]:
                que.append((a, b))
                visited[a][b] = 1
    print(ans)
