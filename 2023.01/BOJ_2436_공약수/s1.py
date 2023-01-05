import sys
sys.stdin = open('input.txt')

def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a
    return a

gcd, lcm = map(int, input().split())
min_sum = sys.maxsize
d = lcm // gcd
ans = []
for a in range(1, int(d**0.5)+1):
    b = int(d / a)
    if not d % a and find_gcd(a, b) == 1:
        if b - a < min_sum:
            min_sum = b - a
            ans = [a*gcd, b*gcd]
print(*ans)