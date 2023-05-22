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

n, m = map(int, input().split())
p = list(range(n+1))
edge_cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
        edge_cnt += 1

edges = []
for i in range(1, n+1):
    row = list(map(int, input().split()))
    if i == 1:
        continue
    for j in range(i+1, n+1):
        edges.append((i, j, row[j-1]))
edges.sort(key=lambda x:x[2])

ans = 0
new = []
for i in range(len(edges)):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        ans += c
        edge_cnt += 1
        new.append((a, b))
    if edge_cnt == n-1:
        break

print(ans, len(new))
for a, b in new:
    print(a, b)









