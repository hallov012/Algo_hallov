import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
que = deque(list(range(1, n+1)))
ans = []
cnt = 1
while que:
    num = que.popleft()
    if not cnt % k:
        ans.append(num)
    else:
        que.append(num)
    cnt += 1


answer = "<"
for i in range(n):
    if i == n-1:
        answer += str(ans[i])
    else:
        answer += str(ans[i]) + ", "
answer += ">"
print(answer)