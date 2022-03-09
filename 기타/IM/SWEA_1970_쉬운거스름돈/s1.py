import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * len(money)
    for i in range(len(money)):
        while n >= money[i]:
            cnt[i] += 1
            n -= money[i]
    print(f'#{tc}')
    print(*cnt)

