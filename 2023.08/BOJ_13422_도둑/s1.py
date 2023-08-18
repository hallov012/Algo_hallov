import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    money = list(map(int, input().split()))

    # n == m 이면 투 포인터로 보는 경우 모두 같은 집들이기 때문에 예외로 처리해줘야 함
    if n == m:
        if sum(money) < k:
            print(1)
        else:
            print(0)
        continue

    cnt = sum(money[:m])
    ans = 0
    if cnt < k:
        ans += 1
    l, r = 0, m-1
    while l < n-1:
        cnt -= money[l]
        l += 1
        r += 1
        if r == n:
            r %= n
        cnt += money[r]
        if cnt < k:
            ans += 1
    print(ans)


