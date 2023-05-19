import sys
sys.stdin = open('input.txt')

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    p[x] = y

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
built = 0
edges = []
ans = 0
p = list(range(n))
for i in range(n):
    for j in range(i+1, n):
        # 이미 건설된 도로
        if arr[i][j] < 0:
            ans += -arr[i][j]
            if find(i) != find(j):
                union(i, j)
                built += 1
        else:
            edges.append((i, j, arr[i][j]))
edges.sort(key=lambda x:x[2])

cnt = 0
new = []
for i in range(len(edges)):
    a, b, c = edges[i]
    if find(a) != find(b):
        union(a, b)
        ans += c
        cnt += 1
        new.append((a, b))

print(ans, cnt)
for a, b in new:
    print(a+1, b+1)