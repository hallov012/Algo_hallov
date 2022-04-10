import sys
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

input = sys.stdin.readline
n, m = map(int, input().split())
p = list(range(n+1))
ans = 0
for i in range(m):
    x, y = map(int, input().split())
    if find(x) == find(y):
        ans = i+1
        break
    else:
        union(x, y)
print(ans)


