import sys
sys.stdin = open('input.txt')

n = int(input())
box = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    temp = []
    for j in range(i):
        if box[i] > box[j]:
            temp.append(dp[j] + 1)
    if not temp:
        dp[i] = 1
    else:
        dp[i] = max(temp)
print(max(dp))