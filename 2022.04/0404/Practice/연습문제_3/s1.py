import sys

def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[y] = x

def kruskal():
    global ans
    edge_cnt = idx = 0
    while edge_cnt != v:
        x = edges[idx][0]
        y = edges[idx][1]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1

sys.stdin = open('input.txt')
ans = 0
v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
p = [0] * (v + 1)
edges = sorted(edges, key=lambda x: x[2])
for i in range(v + 1):
    make_set(i)
kruskal()
print(ans)