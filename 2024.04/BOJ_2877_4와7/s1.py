import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
k = 1
ans = deque()

if n == 1:
    print(4)
elif n == 2:
    print(7)
else:
    while n:
        if n % 2:
            ans.appendleft(4)
        else:
            ans.appendleft(7)
        n /= 2

    ans.popleft()

