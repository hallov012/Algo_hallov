import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

def kruskal():
    global ans, edges_cnt
    idx = 0
    while edges_cnt < n-1:
        x = edges[idx][0]
        y = edges[idx][1]
        cost = edges[idx][2]
        if find(x) != find(y):
            union(x, y)
            ans += cost + (t * edges_cnt)
            edges_cnt += 1
        idx += 1

input = sys.stdin.readline

n, m, t = map(int, input().split())
p = list(range(n+1))
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
ans, edges_cnt = 0, 0
kruskal()
print(ans)
