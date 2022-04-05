import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
d = [[0] * (k+1) for _ in range(n+1)]
subjects = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, k+1):
        w = subjects[i][0]
        v = subjects[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)
print(d[n][k])