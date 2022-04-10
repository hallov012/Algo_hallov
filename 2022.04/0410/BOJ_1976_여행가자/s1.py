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
        p[y] = x
    else:
        p[x] = y

input = sys.stdin.readline

n = int(input())
m = int(input())
p = list(range(n+1))
for i in range(1, n+1):
    path = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if path[j]:
            union(i, j)
plan = list(map(int, input().split()))
ans = set([find(i) for i in plan])
if len(ans) == 1:
    print("YES")
else:
    print("NO")