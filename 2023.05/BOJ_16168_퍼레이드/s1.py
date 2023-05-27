import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(node):
    for next in g[node]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)

input = sys.stdin.readline

v, e = map(int, input().split())
degree = [0] * (v+1)
visited = [0] * (v+1)
g = defaultdict(list)

for _ in range(e):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1
    g[a].append(b)
    g[b].append(a)

odd = 0
for i in range(1, v+1):
    if degree[i] % 2:
        odd += 1

if odd == 0 or odd == 2:
    visited[1] = 1
    dfs(1)
    for i in range(1, v+1):
        if not visited[i]:
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')

