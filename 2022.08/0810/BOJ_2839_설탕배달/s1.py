import sys
sys.stdin = open('input.txt')

n = int(input())
cnt = 0
while True:
    if n % 5:
        n = n-3
        cnt += 1
    elif n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    if n < 0:
        print(-1)
        break