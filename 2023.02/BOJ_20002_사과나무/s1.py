import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
ans = -sys.maxsize
for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            temp = dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
            ans = max(ans, temp)

print(ans)