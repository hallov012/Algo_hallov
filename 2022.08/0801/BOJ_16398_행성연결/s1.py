import sys
sys.stdin = open('input.txt')

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        p[y] = x
    else:
        p[x] = p[y]

def kruskal():
    ans = 0
    idx = 0
    edge_cnt = 0
    while edge_cnt < n-1:
        x = edges[idx][0]
        y = edges[idx][1]
        cost = edges[idx][2]
        if find(x) != find(y):
            union(x, y)
            edge_cnt += 1
            ans += cost
        idx += 1
    return ans

input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
p = list(range(n+1))
edges = []

for i in range(n):
    for j in range(i+1, n):
        edges.append((i, j, g[i][j]))

edges.sort(key=lambda x:x[2])
ans = kruskal()
print(ans)