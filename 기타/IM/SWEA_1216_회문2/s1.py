import sys
sys.stdin = open('input.txt')

def check_cir(str, k):
    middle = k // 2
    if k % 2:
        ans = 1
    else:
        ans = 0
    i = 0
    while i < middle:
        if str[i] == str[k-i-1]:
            ans += 2
        else:
            break
        i += 1
    if ans == k:
        return k
    else:
        return False

for tc in range(1, 11):
    n = int(input())
    data = [input() for _ in range(100)]
    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                check = ''
                if j + k > 100:
                    break
                else:
                    for a in range(k):
                        check += data[i][j+a]
                    if check_cir(check, k) > ans:
                        ans = check_cir(check, k)
    for j in range(100):
        col_str = ''
        for i in range(100):
            col_str += data[i][j]
            for a in range(100):
                for k in range(100):
                    check = ''
                    if j + k > 100:
                        break
                    else:
                        for b in range(k):
                            check += data[i][j+b]
                        if check_cir(check, k) > ans:
                            ans = check_cir(check, k)
    print(f'#{tc} {ans}')


