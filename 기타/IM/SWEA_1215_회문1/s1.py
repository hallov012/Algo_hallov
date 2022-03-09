import sys
sys.stdin = open('input.txt')

def check_cir(str, n):
    middle = n // 2
    if n % 2:
        ans = 1
    else:
        ans = 0
    i = 0
    while i < middle:
        if str[i] == str[n-i-1]:
            ans += 2
        else:
            break
        i += 1
    if ans == n:
        return True
    else:
        return False

for tc in range(1, 11):
    n = int(input())
    data = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            check = ''
            for a in range(n):
                check += data[i][j+a]
            if check_cir(check, n):
                cnt += 1
    for j in range(8):
        col_str = ''
        for i in range(8):
            col_str += data[i][j]
        for a in range(8-n+1):
            check = ''
            for b in range(n):
                check += col_str[a+b]
            if check_cir(check, n):
                cnt += 1
    print(f'#{tc} {cnt}')




