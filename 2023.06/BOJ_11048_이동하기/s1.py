import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m+1)]
for _ in range(n):
    line = list(map(int, input().split()))
    arr.append([0] + line)
# 오른쪽, 아래, 오른쪽 아래 대각선으로 이동 가능
dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = arr[1][1]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + arr[i][j]
print(dp[n][m])