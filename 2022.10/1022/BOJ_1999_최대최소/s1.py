import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, b, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n-b+1):
    for j in range(n-b+1):
        max_num = 0
        min_num = sys.maxsize
        for p in range(i, i+b):
            for q in range(j, j+b):
                max_num = max(max_num, data[p][q])
                min_num = min(min_num, data[p][q])
        dp[i][j] = max_num - min_num
for _ in range(k):
    x, y = map(int, input().split())
    print(dp[x-1][y-1])