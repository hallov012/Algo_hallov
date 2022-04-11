import sys, math
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

def kruskal():
    global ans
    edge_cnt = idx = 0
    while edge_cnt != n-1:
        x = edges[idx][0]
        y = edges[idx][1]
        if find(x) != find(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1

input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
        edges.append((i+1, j+1, d))
edges = sorted(edges, key=lambda x: x[2])
p = list(range(n+1))
ans = 0
kruskal()
print(round(ans, 2))