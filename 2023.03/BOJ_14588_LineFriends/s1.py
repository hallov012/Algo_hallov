import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
questions = [list(map(int, input().split())) for _ in range(q)]
g = [[sys.maxsize] * n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        l1, r1 = lines[i]
        l2, r2 = lines[j]
        if (l1 <= l2 <= r1) or (l1 <= r2 <= r1) or (l2 <= l1 and r1 <= r2):
            g[i][j] = 1
            g[j][i] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            g[j][k] = min(g[j][k], g[j][i]+g[i][k])

for a, b in questions:
    a -= 1
    b -= 1
    if g[a][b] == sys.maxsize:
        print(-1)
    else:
        print(g[a][b])
