import sys
sys.stdin = open('input.txt')

n = int(input())
if n <= 3:
    if n == 1 or n == 3:
        print('CY')
    else:
        print('SK')
    exit()

dp = [0] * (n+1)
dp[1] = dp[3] = 1
for i in range(4, n+1):
    if dp[i-1] or dp[i-3]:
        continue
    else:
        dp[i] = 1

print('CY' if dp[n] else 'SK')
