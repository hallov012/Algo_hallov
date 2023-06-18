import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
left, right = 0, max(nums)
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for num in nums:
        if num > mid:
            cnt += mid
        else:
            cnt += num
    if cnt <= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)