import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
total = 0

p = list(range(n+1))
cnt = 0
edges_cnt = 0
for idx in range(m):
    x = edges[idx][0]
    y = edges[idx][1]
    cost = edges[idx][2]
    if find(x) != find(y):
        union(x, y)
    else:
        cnt += cost

p_set = set()
for i in range(1, n+1):
    p_set.add(find(i))

if len(p_set) == 1:
    print(cnt)
else:
    print(-1)