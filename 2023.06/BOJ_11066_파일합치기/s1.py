import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    sub_sum = [0] * (n+1)
    for i in range(n+1):
        sub_sum[i] = sub_sum[i-1] + data[i]

    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(2, n+1): # 부분 파일의 길이
        for j in range(1, n+2-i): # 시작하는 파일의 넘버: n+1 - (i-1)
            min_sum = sys.maxsize
            for k in range(i-1):
                temp = dp[j][j+k] + dp[j+k+1][j+i-1]
                min_sum = min(min_sum, temp)
            dp[j][j+i-1] = min_sum + sub_sum[j+i-1] - sub_sum[j-1]
    print(dp[1][n])