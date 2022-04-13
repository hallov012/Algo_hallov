import sys
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
p = list(range(n+1))
planets = []
edges = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append([x, y, z, i])
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, n):
        d = abs(planets[j-1][i] - planets[j][i])
        edges.append([planets[j-1][3], planets[j][3], d])
edges.sort(key=lambda x: x[2])
ans = 0
kruskal()
print(ans)