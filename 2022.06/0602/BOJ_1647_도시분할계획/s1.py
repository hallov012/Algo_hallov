import sys
sys.stdin = open('input.txt')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for _ in range(m):
    a, b, c = map(int, input().split())
    g.append((a, b, c))
g.sort(key=lambda x: x[2])
parent = list(range(n+1))
ans = 0
selected = []
for a, b, c in g:
    # 서로 다른 부모를 가지고 있다면 그 두 집을 연결하는 길은 가지고 있어야한다
    if find(a) != find(b):
        union(a, b)
        ans += c
        selected.append(c)
# 마지막 길을 제거하며 마을을 두개로 분리
ans -= selected[-1]
print(ans)

