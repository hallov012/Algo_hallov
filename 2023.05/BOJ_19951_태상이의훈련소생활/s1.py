import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
h_list = list(map(int, input().split()))
cnt = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    cnt[a-1] += k
    cnt[b] -= k
dp = [0] * (n+1)
dp[0] = cnt[0]
for i in range(1, n+1):
    dp[i] = dp[i-1] + cnt[i]
for i in range(n):
    h_list[i] += dp[i]
print(*h_list)