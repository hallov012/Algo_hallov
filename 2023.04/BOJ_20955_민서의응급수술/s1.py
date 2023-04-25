import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(range(n+1))
ans = 0
for _ in range(m):
    u, v = map(int, input().split())
    if find(u) == find(v):
        ans += 1
    else:
        union(u, v)

for i in range(1, n):
    if find(i) != find(i+1):
        union(i, i+1)
        ans += 1
print(ans)


