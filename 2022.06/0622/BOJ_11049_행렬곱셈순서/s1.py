import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)
dp = [[0] * n for _ in range(n)]

for j in range(1, n): # 대각선에서 얼마나 떨어져있는지 (0일땐 자신과 곱하는 것이므로 빼줌)
    for i in range(n-j): # 몇번째 열인지
        if j == 1:
            dp[i][i+j] = matrix[i][0] * matrix[i][1] * matrix[i+j][1]
        else:
            dp[i][i+j] = 2 ** 32
            for k in range(i, i+j):
                dp[i][i+j] = min(dp[i][i+j],
                                 dp[i][k] + dp[k+1][i+j] + matrix[i][0] * matrix[k][1] * matrix[i+j][1])
print(dp[0][n-1])
