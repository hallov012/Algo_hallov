import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if (i, j) == (n-1, n-1):
            break
        move = arr[i][j]
        if j + move < n:
            dp[i][j+move] += dp[i][j]
        if i + move < n:
            dp[i+move][j] += dp[i][j]
print(dp[-1][-1])