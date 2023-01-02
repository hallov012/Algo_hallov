import sys
sys.stdin = open('input.txt')

def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a = a % b
        a, b = b, a
    return a

n = int(input())
data = list(map(int, input().split()))
first = data[0]
for i in range(1, n):
    gcd = find_gcd(first, data[i])
    print(f"{first//gcd}/{data[i]//gcd}")

