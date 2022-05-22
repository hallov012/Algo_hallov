import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1, -1, -1):
    while coins[i] <= k:
        a = k // coins[i]
        ans += a
        k -= coins[i] * a
    if k == 0:
        break
print(ans)