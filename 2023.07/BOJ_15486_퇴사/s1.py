import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i-1], dp[i])
    t, p = data[i-1]
    if i + t - 1 <= n:
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])

print(max(dp))