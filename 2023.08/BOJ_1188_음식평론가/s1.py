import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)

n, m = map(int, input().split())
ans = m - gcd(n, m)
print(ans)