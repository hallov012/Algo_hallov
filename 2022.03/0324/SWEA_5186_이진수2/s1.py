import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = float(input())
    ans = ''
    for i in range(-1, -13, -1):
        if num >= 2 ** i:
            ans += '1'
            num -= 2 ** i
            if num == 0:
                break
        else:
            ans += '0'
    if num == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')

