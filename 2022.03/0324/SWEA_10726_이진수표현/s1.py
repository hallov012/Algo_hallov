import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    bin_num = ''
    N = 30
    for i in range(N, -1, -1):
        if m >= 2 ** i:
            bin_num += '1'
            m -= 2 ** i
        else:
            bin_num += '0'

    check = True
    for j in range(n):
        if bin_num[-1 - j] == '0':
            check = False
            break

    if check:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')


