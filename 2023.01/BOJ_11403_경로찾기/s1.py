import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][k] and g[k][j]:
                g[i][j] = 1

for row in g:
    print(*row)