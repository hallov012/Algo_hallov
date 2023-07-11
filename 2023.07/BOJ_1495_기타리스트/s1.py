import sys
sys.stdin = open('input.txt')

n, s, m = map(int, input().split())
v_lst = list(map(int, input().split()))
dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j]:
            if j + v_lst[i] <= m:
                dp[i+1][j + v_lst[i]] = 1
            if j - v_lst[i] >= 0:
                dp[i+1][j - v_lst[i]] = 1

ans = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        ans = i
        break
print(ans)