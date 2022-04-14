import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

nums = []
for tc in range(T):
    nums.append(int(input()))

max_num = max(nums)
for i in range(6, max_num+1):
    dp[i] = dp[i-1] + dp[i-5]

for num in nums:
    print(dp[num])
