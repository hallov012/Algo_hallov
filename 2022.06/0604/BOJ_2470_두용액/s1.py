import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
min_ans = 2000000000
ans = []
left, right = 0, n-1
while left < right:
    check = nums[left] + nums[right]
    if abs(check) < min_ans:
        min_ans = abs(check)
        ans = [nums[left], nums[right]]
    if check < 0:
        left += 1
    elif check > 0:
        right -= 1
    else:
        break

print(*ans)