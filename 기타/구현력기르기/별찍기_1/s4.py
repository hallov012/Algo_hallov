import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(n):
    star = ''
    star += ' ' * i
    star += '*' * (n-i)
    print(star)
