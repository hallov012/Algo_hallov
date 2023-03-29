import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    else:
        p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
courses = list(map(int, input().split()))
for i in range(n+1):
    p[i] = find(p[i])
ans = -1
before = 0
for num in courses:
    if before != p[num]:
        ans += 1
        before = p[num]
print(ans)