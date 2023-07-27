import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**7)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y, d):
    global edge_cnt, cnt
    x, y = find(x), find(y)
    if x != y:
        p[x] = y
        edge_cnt += 1
        cnt += d

input = sys.stdin.readline

n, m, k = map(int, input().split())
s_lst = [0] + list(map(int, input().split()))

if m <= 1:
    print('YES')
    exit()

in_construction = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == 1 and b == n:
        in_construction[b] = True
    else:
        in_construction[a] = True

edges = []
for i in range(1, n+1):
    edges.append((i, s_lst[i]))

p = list(range(n+2))
edge_cnt = 0
cnt = 0

for i in range(1, n+1):
    if i == n:
        if not in_construction[i]:
            union(i, 1, 0)
    else:
        if not in_construction[i]:
            union(i, i+1, 0)

edges.sort(key=lambda x:x[1])
ans = False
for x, d in edges:
    if find(x) != find(n+1):
        union(x, n+1, d)
    if cnt > k:
        break
    if edge_cnt == n:
        ans = True
        break

print('YES' if ans else 'NO')