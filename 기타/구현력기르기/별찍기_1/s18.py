import sys
sys.stdin = open('input.txt')

def star(len):
    if len == 1:
        g[0] = ['*']
        return
    if len == 2:
        g[:3] = ['  *  ', '*' * 3, '*' * 5]
        return



n = int(input())
g = ['' for _ in range(2 ^ n - 1)]
star(n)
for i in range(2^n-1):
    print(g[i])