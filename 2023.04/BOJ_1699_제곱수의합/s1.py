import sys
sys.stdin = open('input.txt')

n = int(input())
dp = list(range(n+1))
for i in range(1, n+1):
    for j in range(1, i):
        if j*j <= i:
            if dp[i] > dp[i-j*j] + 1:
                dp[i] = dp[i-j*j] + 1
        else:
            break
print(dp[-1])
