import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

a, b, c = map(int, input().split())
def dnc(a, b, c):
    if b == 1:
        return a % c
    elif not b % 2:
        return (dnc(a, b//2, c) ** 2) % c
    else:
        return ((dnc(a, b//2, c) ** 2) * a) % c

ans = dnc(a, b, c)
print(ans)




