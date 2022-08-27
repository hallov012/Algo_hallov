import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if y > x:
        p[y] = x
    else:
        p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
upper = 0
for _ in range(m+1):
    a, b, c = map(int, input().split())
    if c == 0:
        edges.append((a, b, 1))
        upper += 1
    else:
        edges.append((a, b, 0))

min_edges = sorted(edges, key=lambda x: x[2])
p = list(range(n + 1))
min_ans = 0
edges_cnt = 0
idx = 0
while edges_cnt < n:
    x = min_edges[idx][0]
    y = min_edges[idx][1]
    cost = min_edges[idx][2]
    if find(x) != find(y):
        union(x, y)
        edges_cnt += 1
        min_ans += cost
    idx += 1

max_edges = sorted(edges, key=lambda x: x[2], reverse=True)
p = list(range(n + 1))
max_ans = 0
edges_cnt = 0
idx = 0
while edges_cnt < n:
    x = max_edges[idx][0]
    y = max_edges[idx][1]
    cost = max_edges[idx][2]
    if find(x) != find(y):
        union(x, y)
        edges_cnt += 1
        max_ans += cost
    idx += 1

print(max_ans ** 2 - min_ans ** 2)