import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
left, right = 0, 0
ans = sys.maxsize
while left < n and right < n:
    temp = nums[right] - nums[left]
    if temp >= m:
        ans = min(ans, temp)
        left += 1
    else:
        right += 1
print(ans)

