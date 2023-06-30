import sys
sys.stdin = open('input.txt')

n = int(input())
m = 1000
dp = [0] * (m+1)
# 처음에 낼 수 있는 돌의 수
dp[1] = dp[3] = 1
for i in range(4, n+1):
    # 이전이 자신의 차례였다면 돌을 낼 수 없음
    if dp[i-1] or dp[i-3]:
        continue
    else:
        dp[i] = 1

print('SK' if dp[n] else 'CY')