import sys
sys.stdin = open('input.txt')

n = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(n+1):
    for j in range(1, i+1):
        temp = dp[i-j] + cost[j]
        dp[i] = max(dp[i], temp)
print(dp[-1])
