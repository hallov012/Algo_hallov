import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
ans = 0
d = 1
ni = 9

while k > d * ni:
    k -= d * ni
    ans += ni
    d += 1
    ni *= 10

ans = ans + 1 + (k-1)//d
if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%d])




