import sys
sys.stdin = open('input.txt')

n = int(input())
star = ['' for _ in range(2*n-1)]
for i in range(n):
    if not i:
        star[i] = ' ' * (n-i-1) + '*'
    else:
        star[i] = ' ' * (n-i-1) + '*' + ' ' * (2*i-1) + '*'
for i in range(n):
    print(star[i])