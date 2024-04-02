import sys
sys.stdin = open('input.txt')

n = int(input())
scv = list(map(int, input().split()))
if len(scv) < 3:
    for _ in range(3-len(scv)):
        scv.append(0)

dp = [[[sys.maxsize] * 61 for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 0

cases = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] != sys.maxsize:
                for a, b, c in cases:
                    x = max(i-a, 0)
                    y = max(j-b, 0)
                    z = max(k-c, 0)
                    dp[x][y][z] = min(dp[x][y][z], dp[i][j][k] + 1)
print(dp[0][0][0])
