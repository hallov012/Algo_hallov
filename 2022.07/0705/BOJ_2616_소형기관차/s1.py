import sys
sys.stdin = open('input.txt')

# 소형 기관차 3대가 최대로 운송할 수 있는 손님 수 구하기
n = int(input())
data = [0] + list(map(int, input().split()))
k = int(input())
dp = [[0] * (n+1) for _ in range(4)]

for i in range(4):
    for j in range(1, n+1):
        if i == 0: # 누적합을 dp[0]을 저장
            dp[i][j] = dp[i][j-1] + data[j]
        elif j < i*k:
            continue
        elif i == 1:
            dp[i][j] = max(dp[i][j-1], dp[0][j]-dp[0][j-k])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + dp[0][j] - dp[0][j-k])
print(dp[3][n])
