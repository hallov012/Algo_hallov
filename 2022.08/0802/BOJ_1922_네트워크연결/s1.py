import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

n = int(input())
m = int(input())
p = list(range(n+1))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
ans = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)