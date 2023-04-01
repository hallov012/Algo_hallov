import sys
sys.stdin = open('input.txt')

n = int(input())
if n == 1 or n == 2:
    print(1)
    exit()
dp = [0] * n
dp[0] = dp[1] = 1
for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])

