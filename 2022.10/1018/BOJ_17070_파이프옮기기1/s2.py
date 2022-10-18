import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# dp[0] 가로, dp[1] 세로, dp[2] 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
# 첫 행 초기화
for i in range(2, n):
    if not arr[0][i]:
        dp[0][0][i] = dp[0][0][i-1]

for x in range(1, n):
    for y in range(1, n):
        if not arr[x][y] and not arr[x][y-1] and not arr[x-1][y]:
            dp[2][x][y] = dp[0][x-1][y-1] + dp[1][x-1][y-1] + dp[2][x-1][y-1]
        if not arr[x][y]:
            dp[0][x][y] = dp[0][x][y-1] + dp[2][x][y-1]
            dp[1][x][y] = dp[1][x-1][y] + dp[2][x-1][y]

ans = 0
for i in range(3):
    ans += dp[i][n-1][n-1]
print(ans)