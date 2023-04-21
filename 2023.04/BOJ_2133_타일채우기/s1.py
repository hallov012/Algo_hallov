import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * (n+1)
if n < 2:
    print(0)
    exit()
dp[2] = 3
cnt = 0
for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * 3 + 2
    dp[i] += cnt * 2
    cnt += dp[i-2]
print(dp[n])