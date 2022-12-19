import sys, math
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

n, m = map(int, input().split())
city = [0] + [list(map(int, input().split())) for _ in range(n)]
p = list(range(n+1))
edge_cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
        edge_cnt += 1
edges = []
for i in range(1, n+1):
    a, b = city[i]
    for j in range(1, n+1):
        if i != j:
            c, d = city[j]
            dist = (a-c)**2 + (b-d)**2
            edges.append((i, j, dist))
edges.sort(key=lambda x:x[2], reverse=True)
print(edges)
ans = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
        edge_cnt += 1
    if edge_cnt == n-1:
        break

print(ans)
