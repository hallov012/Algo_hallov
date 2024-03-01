import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, q, c = map(int, input().split())
cap = [0] + list(map(int, input().split()))

"""
B: 뒤로가기
F: 앞으로 가기
A: 접속
C: 압축

b_que => now > f_que
"""
f_que = deque()
b_que = deque()
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
    elif command == 'A':
        page = int(page[0])
        if now == -1:
            now = page
        else:
            b_que.append(now)
            now = page
            cnt -= sum(f_que)
            f_que = deque()
        cnt += cap[page]
        while cnt > c:
            delete = b_que.popleft()
            cnt -= cap[delete]
    elif command == 'C':
        b_p = -1
        n_b_que = deque()
        while b_que:
            p = b_que.popleft()
            if p == b_p:
                cnt -= cap[p]
            else:
                b_p = p
                n_b_que.append(p)
        b_que = n_b_que

print(now)
if b_que:
    print(' '.join(map(str, reversed(b_que))))
else:
    print(-1)
if f_que:
    print(' '.join(map(str, reversed(f_que))))
else:
    print(-1)




