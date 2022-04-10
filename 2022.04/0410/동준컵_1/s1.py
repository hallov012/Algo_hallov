import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    coins = sorted(list(map(int, input().split())), reverse=True)
    ans, i = 0, 0
    while m > 0:
        ans += m // coins[i]
        m -= coins[i] * (m//coins[i])
        i += 1
    print(f'{tc} {ans}')
