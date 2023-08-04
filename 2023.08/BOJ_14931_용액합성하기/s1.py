import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
left, right = 0, n-1
ans = sys.maxsize
while left < right:
    temp = nums[left] + nums[right]
    if abs(ans) > abs(temp):
        ans = temp
    if temp < 0:
        left += 1
    else:
        right -= 1

print(ans)