import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(n):
    num = nums[i]
    left, right = 0, n-1
    if left == i:
        left += 1
    if right == i:
        right -= 1
    while left < right:
        check = nums[left] + nums[right]
        if check == num:
            ans += 1
            break
        elif check > num:
            right -= 1
            if right == i:
                right -= 1
        else:
            left += 1
            if left == i:
                left += 1
print(ans)

