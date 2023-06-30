import sys
sys.stdin = open('input.txt')

n = int(input())
if n <= 5:
    if n == 2 or n == 5:
        print(1)
    elif n == 4:
        print(2)
    else:
        print(-1)
    exit()

inf = 1e9
dp = [inf] * (n+1)
dp[2] = dp[5] = 1
dp[4] = 2

for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1
print(dp[n] if dp[n] < inf else -1)