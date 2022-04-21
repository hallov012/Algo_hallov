import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

ans = 0
coins = [int(input()) for _ in range(n)]
for i in range(n-1, -1, -1):
    if coins[i] <= k:
        a = k // coins[i]
        ans += a
        k -= a * coins[i]
        if k == 0:
            print(ans)
