import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 1
for _ in range(m):
    a, b, t = map(int, input().split())
    dp[a][b] = t

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

k = int(input())
c_lst = list(map(int, input().split()))

ans = [sys.maxsize, []]
for i in range(1, n+1):
    max_num = 0
    for c in c_lst:
        if dp[c][i] == sys.maxsize or dp[i][c] == sys.maxsize:
            break
        else:
            temp = dp[c][i] + dp[i][c]
            max_num = max(temp, max_num)
    else:
        if max_num < ans[0]:
            ans = [max_num, [i]]
        elif max_num == ans[0]:
            ans[1].append(i)

print(*ans[1])