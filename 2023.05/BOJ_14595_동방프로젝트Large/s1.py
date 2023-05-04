import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        p[x] = y

n = int(input())
m = int(input())
p = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    while find(a) != find(b):
        n -= 1
        c = find(a) + 1
        union(a, b)
        a = c
print(n)