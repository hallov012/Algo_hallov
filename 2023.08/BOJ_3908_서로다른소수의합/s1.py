import sys, math
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
m = 1121
nums = [True] * m
nums[1] = False
for i in range(2, int(math.sqrt(m)) + 1):
    if nums[i]:
        for j in range(2*i, m, i):
            nums[j] = False

# x라는 수를 y개의 조합으로 만드는 것
dp = [[0] * 15 for _ in range(m)]
dp[0][0] = 1

# 한 소수 i를 가지고
for i in range(1, m):
    if nums[i]:
        # 최댓값부터 i까지 역순으로 돌면서
        for j in range(m-1, i-1, -1):
            # j-i 라는 수를 k-1개의 조합으로 만들수 있었던 경우의 수를 더해줌
            for k in range(1, 15):
                dp[j][k] += dp[j-i][k-1]

for _ in range(T):
    n, k = map(int, input().split())
    print(dp[n][k])



