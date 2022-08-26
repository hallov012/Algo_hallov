import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
for i in range(3):
    dp = [[sys.maxsize] * 3 for _ in range(n)]
    dp[0][i] = cost[0][i]
    for j in range(1, n):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])
    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])
print(ans)