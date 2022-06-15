import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        a, b = 0, n-1
        flag = False
        while a < b:
            check = lego[a] + lego[b]
            if check == x:
                print(f'yes {lego[a]} {lego[b]}')
                flag = True
                break
            elif check < x:
                a += 1
            else:
                b -= 1
        if not flag:
            print('danger')
    except:
        break

