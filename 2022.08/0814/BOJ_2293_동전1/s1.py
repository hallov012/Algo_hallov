import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] += dp[j-coin]
print(dp[k])