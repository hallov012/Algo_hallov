import sys
sys.stdin = open('input.txt')

n = int(input())

for i in range(n):
    star = ' ' * i + '*' * ((n-1-i)*2 + 1)
    print(star)