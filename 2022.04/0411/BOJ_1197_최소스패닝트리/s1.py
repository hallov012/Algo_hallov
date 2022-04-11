import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[y] = x

def kruskal():
    global ans
    edge_cnt = idx = 0
    while edge_cnt != v-1:
        x = edges[idx][0]
        y = edges[idx][1]
        if find(x) != find(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
edges = sorted(edges, key=lambda x: x[2])
p = list(range(v+1))
ans = 0
kruskal()
print(ans)