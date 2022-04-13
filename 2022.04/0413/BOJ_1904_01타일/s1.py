import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * (n+1)
if n == 1:
    print(1)
    exit()
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746
print(dp[-1])


