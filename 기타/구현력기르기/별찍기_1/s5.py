import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(n):
    star = ''
    star += ' ' * (n-i-1) + '*' * (2*i+1)
    print(star)