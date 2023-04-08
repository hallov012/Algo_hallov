import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(k+1):
        if j > n or j > i:
            break
        if i == j or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)

