import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))
print('<', end='')
while q:
    for _ in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')
    if q:
        print(', ', end='')
    else:
        print('>')


