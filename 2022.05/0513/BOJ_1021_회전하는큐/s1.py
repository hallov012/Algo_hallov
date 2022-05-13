import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
que = deque(list(range(1, n+1)))
cnt = 0
for num in nums:
    while True:
        if que[0] == num:
            que.popleft()
            break
        else:
            if que.index(num) < len(que) / 2:
                while que[0] != num:
                    n = que.popleft()
                    que.append(n)
                    cnt += 1
            else:
                while que[0] != num:
                    n = que.pop()
                    que.appendleft(n)
                    cnt += 1
print(cnt)
