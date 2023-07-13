import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

dp = [0] * (n+1)
dp[0] = dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

if m:
    ans = 1
    before = 0
    for x in vip:
        ans *= dp[x - before - 1]
        before = x
    ans *= dp[n - before]
else:
    ans = dp[n]
print(ans)