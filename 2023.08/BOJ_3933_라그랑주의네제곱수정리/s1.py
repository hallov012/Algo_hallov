import sys, math
sys.stdin = open('input.txt')

m = 2 ** 15
dp = [[0] * 5 for _ in range(m)]
dp[0][0] = 1
for i in range(1, int(math.sqrt(m))+1):
    for j in range(i*i, m):
        for k in range(1, 5):
            dp[j][k] += dp[j-i*i][k-1]

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(dp[n]))
