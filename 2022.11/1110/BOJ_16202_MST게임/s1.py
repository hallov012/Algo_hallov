import sys
from collections import deque
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

n, m, k = map(int, input().split())
w = 1
edges = deque()
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((a, b, w))
    w += 1

ans = []

for i in range(k):
    cnt = 0
    edges_cnt = 0
    p = list(range(n+1))
    for idx in range(len(edges)):
        x = edges[idx][0]
        y = edges[idx][1]
        cost = edges[idx][2]
        if find(x) != find(y):
            union(x, y)
            edges_cnt += 1
            cnt += cost
        if edges_cnt == n-1:
            ans.append(cnt)
            edges.popleft()
            break
    else:
        ans.append(0)
        break

if len(ans) < k:
    while len(ans) != k:
        ans.append(0)
print(*ans)