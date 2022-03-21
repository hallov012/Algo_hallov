import sys
sys.stdin = open('input.txt')

def factorial(num):
    ans = num
    while num > 1:
        num -= 1
        ans *= num
    return ans

n, m = map(int, input().split())
if n == m:
    print(1)
    exit()
result = factorial(n) // (factorial(m) * factorial(n-m))
print(result)

