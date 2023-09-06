import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        p[x] = y

n, m = map(int, input().split())
g = defaultdict(list)
p = list(range(n+1))
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    union(a, b)

component = defaultdict(list)
node_cnt = defaultdict(int)
for i in range(1, n+1):
    node = find(i)
    component[node].append(i)
    node_cnt[node] += len(g[i])

ans_lst = []
for key in component.keys():
    ans_lst.append((- node_cnt[key] / len(component[key]), component[key]))
ans_lst.sort()
print(*ans_lst[0][1])


