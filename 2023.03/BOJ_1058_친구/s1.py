import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
g = [[0] * n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y'):
                g[i][j] = 1

ans = 0
for row in g:
    ans = max(ans, sum(row))
print(ans)

