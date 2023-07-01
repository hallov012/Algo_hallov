import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
max_num = 100000
m = 1000000009

dp = [[0] * 3 for _ in range(max_num+1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, max_num+1):
    # 1을 사용
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % m
    # 2를 사용
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % m
    # 3을 사용
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % m


for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % m)