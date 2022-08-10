import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
if n <= 2:
    print(sum(data))
    exit()
dp = [0] * n
dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[2]+data[0], data[2]+data[1], dp[1])
for i in range(3, n):
    dp[i] = max(data[i]+dp[i-2], data[i]+data[i-1]+dp[i-3], dp[i-1])
print(dp[n-1])