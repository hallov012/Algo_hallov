import sys
from collections import deque
sys.stdin = open('input.txt')

n, q, c = map(int, input().split())
cap = [0] + list(map(int, input().split()))

"""
B: 뒤로가기
F: 앞으로 가기
A: 접속
C: 압축

b_que => now > f_que
"""
f_que = b_que = deque()
now = -1
cnt = 0
for _ in range(q):
    command, *page = input().split()
    if command == 'B':
        if b_que:
            f_que.appendleft(now)
            now = b_que.pop()
    elif command == 'F':
        if f_que:
            b_que.append(now)
            now = f_que.popleft()


