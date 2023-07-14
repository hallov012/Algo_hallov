import sys
sys.stdin = open('input.txt')

def find(sx, sy, ex, ey):
    for i in range(sx, ex):
        for j in range(sy, ey):
            if i == sx or j == sy:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

input = sys.stdin.readline

n, m, k = map(int, input().split())
dp = [[0] * m for _ in range(n)]
if k:
    x = (k-1) // m
    y = (k-1) % m

    find(0, 0, x+1, y+1)
    ans = dp[x][y]

    find(x, y, n, m)
    ans *= dp[-1][-1]

else:
    find(0, 0, n, m)
    ans = dp[-1][-1]

print(ans)