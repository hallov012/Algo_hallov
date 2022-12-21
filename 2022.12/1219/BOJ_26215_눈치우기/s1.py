import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
ans = 0
while nums:
    if len(nums) == 1:
        ans += nums[0]
        break
    nums.sort(reverse=True)
    ans += nums[1]
    nums[0] -= nums[1]
    nums[1] = 0
    nums.pop(1)
    if not nums[0]:
        nums.pop(0)

if ans > 1440:
    print(-1)
else:
    print(ans)