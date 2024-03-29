import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

ans = 0
for i in range(1, n+1):
    left = 0
    right = 0
    for j in range(1, n+1):
        if i == j:
            continue
        elif g[i][j]:
            right += 1
        elif g[j][i]:
            left += 1
    if right > n//2 or left > n//2:
        ans += 1
print(ans)