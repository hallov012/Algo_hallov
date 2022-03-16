import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print(f'#{tc}', end=' ')
    for i in range(1, n+1):
        if i ** 3 == n:
            print(i)
            break
        if i ** 3 > n:
            print(-1)
            break