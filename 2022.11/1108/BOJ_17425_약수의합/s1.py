import sys
sys.stdin = open('input.txt')

m = 1000000
dp = [1] * (m+1)
arr_sum = [0] * (m+1)

for i in range(2, m+1):
    j = 1
    while i * j <= m:
        dp[i*j] += i
        j += 1

for i in range(1, m+1):
    arr_sum[i] = arr_sum[i-1] + dp[i]

T = int(input())
ans = []
for _ in range(T):
    n = int(input())
    ans = arr_sum[n]
    print(ans)