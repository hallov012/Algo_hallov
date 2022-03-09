import sys
sys.stdin = open('input.txt')

def star(len):
    div = len // 2
    if len == 3:
        g[-3][:6] = [' '] * 2 + ['*'] + [' '] * 3
        g[-2][:6] = [' ', '*', ' ', '*', ' ', ' ']
        g[-1][:6] = ['*'] * 5 + [' ']
        return
    star(div)
    for i in range(len2-len, len2):
        if i < len2 - len + div:
                g[i][div:div+len] = g[i+div][:len]
        else:
            for j in [0, len]:
                g[i][j:j+len] = g[i][:len]

n = int(input())
g = [[' ' for _ in range(n*2)] for _ in range(n)]
len2 = n
star(n)
for i in range(n):
    a = ''.join(g[i])
    print(a)