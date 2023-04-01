import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n):
    t, p = data[i]
    for j in range(i+t, n+1):
        dp[j] = max(dp[j], dp[i]+p)
print(dp[-1])
