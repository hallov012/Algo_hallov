import sys
sys.stdin = open('input.txt')

n = int(input())
ans = 0
l, r = 0, 0
cnt = 0
while r <= n:
    if cnt == n:
        ans += 1
        r += 1
        cnt += r
    elif cnt < n:
        r += 1
        cnt += r
    else:
        cnt -= l
        l += 1

print(ans)

