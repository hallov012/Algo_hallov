import sys
sys.stdin = open('input.txt')

n, r, c = map(int, input().split())
ans = 0
while n > 1:
    num = (2 ** n) // 2
    if r < num and c < num:
        pass
    elif r < num and c >= num:
        ans += num ** 2
        c -= num
    elif r >= num and c < num:
        ans += num ** 2 * 2
        r -= num
    else:
        ans += num ** 2 * 3
        r -= num
        c -= num
    n -= 1

if r == 0 and c == 0:
    print(ans)
elif r == 0 and c == 1:
    print(ans+1)
elif r == 1 and c == 0:
    print(ans+2)
else:
    print(ans+3)


