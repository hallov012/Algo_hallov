import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

c, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    cnt = max(cnt, data[i][1])

max_cnt = c + cnt + 1
dp = [sys.maxsize] * (max_cnt)
dp[0] = 0
cnt = 0


for a, b in data:
    for i in range(b, max_cnt):
        dp[i] = min(dp[i-b] + a, dp[i])
    print(dp)

print(min(dp[c:]))