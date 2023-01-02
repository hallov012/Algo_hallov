import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a = a % b
        a, b = b, a
    return a

n, s = map(int, input().split())
data = list(map(int, input().split()))
diff = []
for i in range(n):
    diff.append(abs(data[i]-s))
d = diff[0]
for i in range(1, n):
    d = gcd(d, diff[i])
print(d)
