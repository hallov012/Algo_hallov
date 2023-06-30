import math
import sys
sys.stdin = open('input.txt')

n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    min_val = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        if dp[i-j**2] < min_val:
            min_val = dp[i-j**2]
            if min_val == 1:
                break
    dp[i] = min_val + 1

print(dp[n])