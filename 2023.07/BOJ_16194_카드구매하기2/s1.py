import sys
sys.stdin = open('input.txt')

n = int(input())
p_lst = [0] + list(map(int, input().split()))
dp = [sys.maxsize] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        if dp[i] == sys.maxsize:
            dp[i] = dp[i-j] + p_lst[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + p_lst[j])

print(dp[n])