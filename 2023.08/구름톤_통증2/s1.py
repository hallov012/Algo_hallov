import sys
sys.stdin = open('input.txt')

n = int(input())
a, b = map(int, input().split())

dp = [sys.maxsize] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    if i >= b:
        dp[i] = min(dp[i], dp[i-b] + 1)
    if i >= a:
        dp[i] = min(dp[i], dp[i-a] + 1)

print(dp[n] if dp[n] != sys.maxsize else -1)