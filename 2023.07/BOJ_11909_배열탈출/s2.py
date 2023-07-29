"""
dp 사용 => 통과
"""
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        # 왼 쪽에서 오는 것만 가능
        elif i == 0:
            if arr[i][j-1] <= arr[i][j]:
                dp[i][j] = dp[i][j-1] + (arr[i][j] - arr[i][j-1] + 1)
            else:
                dp[i][j] = dp[i][j-1]
        # 위 쪽에서 오는 것만 가능
        elif j == 0:
            if arr[i-1][j] <= arr[i][j]:
                dp[i][j] = dp[i-1][j] + (arr[i][j] - arr[i-1][j] + 1)
            else:
                dp[i][j] = dp[i-1][j]
        # 위 또는 왼 쪽에서 올 수 있는 경우
        else:
            up, left = dp[i-1][j], dp[i][j-1]
            up_gap, left_gap = 0, 0
            if arr[i-1][j] <= arr[i][j]:
                up += arr[i][j] - arr[i-1][j] + 1
            if arr[i][j-1] <= arr[i][j]:
                left += arr[i][j] - arr[i][j-1] + 1
            dp[i][j] = min(up, left)

print(dp[n-1][n-1])