import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(x, d):
    # 방문한 노드 체크
    visited[x] = True
    # 깊이를 저장
    depth[x] = d
    for y in g[x]:
        if not visited[y]:
            p[y][0] = x
            dfs(y, d+1)

def find_parent():
    dfs(1, 0)   # 루트 노드부터
    # 깊이를 하나씩 탐색하면서
    for i in range(1, l):
        # j 노드의 2**i 번째 부모가 뭔지 저장
        for j in range(1, n+1):
            p[j][i] = p[p[j][i-1]][i-1]

def lca(a, b):
    # 깊이가 더 깊은 쪽을 b로 설정
    if depth[a] > depth[b]:
        a, b = b, a

    # b에서 노드를 a와 같은 깊이로 올리며 작업을 수행
    for i in range(l-1, -1, -1):
        # 1 << i = 2 ** i
        # depth[b] - depth[a]는 b를 a로 옮기는데 필요한 횟수
        if depth[b] - depth[a] >= (1 << i):
            b = p[b][i]
    if a == b:
        return a

    # a와 b가 같은 깊이에 위치했을 때 최소 공통 조상을 찾음
    # a와 b를 동시에 부모노드로 이동하며 찾음
    for i in range(l-1, -1, -1):
        if p[a][i] != p[b][i]:
            a = p[a][i]
            b = p[b][i]
    return p[a][0]

input = sys.stdin.readline

n = int(input())
l = 21  # 2 ^ 20 = 1,048,576이니까 최대 깊이는 20
# p[i][j]는 i의 2**j 번째 조상을 저장함
p = [[0] * l for _ in range(n+1)]
depth = [0] * (n+1)
visited = [False] * (n+1)
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

find_parent()

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))