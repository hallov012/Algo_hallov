import sys
sys.stdin = open('input.txt')

imput = sys.stdin.readline

n, m = map(int, input().split())
data_a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
data_b = [list(map(int, input().split())) for _ in range(m)]
ans = [[0] * k for _ in range(n)]
for i in range(n):
    for a in range(k):
        value = 0
        for j in range(m):
            value += data_a[i][j] * data_b[j][a]
        ans[i][a] = value
for line in ans:
    print(*line)