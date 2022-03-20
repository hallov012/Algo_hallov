n, k = map(int, input().split())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

print(int(factorial(n) / factorial(k) / factorial(n - k)))