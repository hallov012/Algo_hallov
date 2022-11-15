import sys
from collections import deque
sys.stdin = open('input.txt')

a, b, c = map(int, input().split())
check = [[0] * 201 for _ in range(201)]
ans = [0] * 201
que = deque([(0, 0, c)])
while que:
    x, y, z = que.popleft()
    if check[x][y]:
        continue
    check[x][y] = 1
    if x == 0:
        ans[z] = 1
    # a => b
    if x + y > b:
        que.append((x+y-b, b, z))
    else:
        que.append((0, x+y, z))
    # a => c
    if x + z > c:
        que.append((x+z-c, y, c))
    else:
        que.append((0, y, x+z))
    # b => a
    if x + y > a:
        que.append((a, x+y-a, z))
    else:
        que.append((x+y, 0, z))
    # b => c
    if y + z > c:
        que.append((x, y+z-c, c))
    else:
        que.append((x, 0, y+z))
    # c => a
    if x + z > a:
        que.append((a, y, x+z-a))
    else:
        que.append((x+z, y, 0))
    # c => b
    if y + z > b:
        que.append((x, b, y+z-b))
    else:
        que.append((x, y+z, 0))

for i in range(201):
    if ans[i]:
        print(i, end=" ")