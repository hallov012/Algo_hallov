import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
for i in range(1, k+1):
    temp = []
    for coin in coins:
        if coin <= i and dp[i-coin] != -1:
            temp.append(dp[i-coin])
    if not temp:
        dp[i] = -1
    else:
        dp[i] = min(temp) + 1
print(dp[k])