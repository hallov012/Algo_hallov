import sys
sys.stdin = open('input.txt')

n = int(input())
star = ['' for _ in range(2*n-1)]
for i in range(n):
    if i == n-1:
        star[i] = '*' * n
    else:
        star[i] = '*' * (i+1)
        star[2*n-i-2] = '*' * (i+1)
for i in range(2*n-1):
    print(star[i])