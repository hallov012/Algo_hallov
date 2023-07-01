import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

w = dp[n]
h = dp[n] + dp[n-1]
ans = (w + h) * 2
print(ans)