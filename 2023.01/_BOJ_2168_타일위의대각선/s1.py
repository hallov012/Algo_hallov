import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a

x, y = map(int, input().split())

