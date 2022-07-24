import sys
from collections import deque
sys.stdin = open('input.txt')

n, k = map(int, input().split())
m = 10 ** 6
ans = 0
que = deque([(n, 0)])
visited = set()
while que:
    now, cnt = que.popleft()
    if cnt == k:
        ans = max(ans, now)
        continue
    nums = list(map(int, str(now)))
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if i == 0 and nums[j] == 0:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            temp = 0
            for num in nums:
                temp = temp*10 + num
            if (temp, cnt+1) not in visited:
                visited.add((temp, cnt+1))
                que.append((temp, cnt+1))
            nums[j], nums[i] = nums[i], nums[j]

if ans > 0:
    print(ans)
else:
    print(-1)
