import sys
sys.stdin = open('input.txt')

n, k = map(int, input(). split())
nums = list(map(int, input().split()))
left, right = 0, 0
cnt = [0] * (max(nums) + 1)
ans = 0
while right < n:
    if cnt[nums[right]] < k:
        cnt[nums[right]] += 1
        right += 1
    else:
        cnt[nums[left]] -= 1
        left += 1
    ans = max(ans, right-left)
print(ans)