import sys
from collections import deque
sys.stdin = open('input.txt')

n, l = map(int, input().split())
nums = list(map(int, input().split()))
ans = []
que = deque()
for i in range(n):
    while que and que[-1] > nums[i]:
        que.pop()
    que.append(nums[i])
    if i >= l and que[0] == nums[i-l]:
        que.popleft()
    ans.append(que[0])
print(*ans)

