import sys
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    elif x < y:
        p[x] = y
    else:
        p[y] = p[x]

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(range(n+1))
for _ in range(m):
    c, a, b = map(int, input().split())
    if c:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
