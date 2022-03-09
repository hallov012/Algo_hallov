import sys
sys.stdin = open('input.txt')

def star(len):
    div = len // 3
    if len == 3:
        g[0][:3] = g[2][:3] = ['*'] * 3
        g[1][:3] = ['*', ' ', '*']
        return
    star(div)
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                for a in range(div):
                    g[div*i+a][div*j:div*(j+1)] = g[a][:div]

n = int(input())
g = [[' ' for _ in range(n)] for _ in range(n)]
star(n)
for i in range(n):
    for j in range(n):
        print(g[i][j], end='')
    print()