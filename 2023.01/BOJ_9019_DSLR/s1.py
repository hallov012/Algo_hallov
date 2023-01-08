import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    n = 10000
    visited = [0] * n
    visited[a] = 1
    que = deque([(a, 1, "")])
    while que:
        now, value, temp = que.popleft()
        next = [0] * 4
        next[0] = (now*2) % n
        next[1] = now-1
        if not next[1]:
            next[1] = 9999

