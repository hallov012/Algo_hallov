import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in range(1, n):
    nums[i] += nums[i-1]
ans = 0
left, right = 0, n-1
total = nums[-1]

for i in range(n-1):
    for j in range(i+1, n):
        forward = nums[j] - nums[i]
        reverse = total - forward
        ans = max(ans, min(forward, reverse))
print(ans)
