import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

input = sys.stdin.readline

n = int(input())
p = list(range(n+1))
for _ in range(n-2):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

ans = []
for i in range(1, n+1):
    if i == p[i]:
        ans.append(i)
print(*ans)
