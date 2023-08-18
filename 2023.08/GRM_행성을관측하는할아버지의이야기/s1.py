import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
big = [[0] * (n+1) for _ in range(n+1)]
small = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # a > b
    big[b][a] = 1
    small[a][b] = 1


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if big[i][k] and big[k][j]:
                big[i][j] = 1
            if small[i][k] and small[k][j]:
                small[i][j] = 1

for i in range(1, n+1):
    print(sum(big[i]), sum(small[i]))

