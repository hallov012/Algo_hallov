import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
ans = 0
left, right = 0, n-1
total = sum(nums)
flag = total//2
stack = nums[0]
left, right = 0, 1
while right <= n:
    if stack < flag:
        if right == n:
            break
        stack += nums[right]
        right += 1
    else:
        ans = max(ans, min(stack, total-stack))
        stack -= nums[right-1]
        ans = max(ans, min(stack, total-stack))
        stack += nums[right-1] - nums[left]
        left += 1
print(ans)