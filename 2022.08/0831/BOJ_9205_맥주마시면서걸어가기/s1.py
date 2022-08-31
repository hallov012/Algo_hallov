import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sx, sy = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    ex, ey = map(int, input().split())
    # 0은 집, n은 목적지
    visited = [0] * (n+1)
    que = deque([(sx, sy)])
    flag = False
    while que:
        x, y = que.popleft()
        if abs(ex-x) + abs(ey-y) <= 1000:
            flag = True
            break
        for i in range(n):
            nx, ny = store[i]
            if abs(nx-x) + abs(ny-y) <= 1000 and not visited[i]:
                visited[i] = 1
                que.append((nx, ny))
    if flag:
        print('happy')
    else:
        print('sad')