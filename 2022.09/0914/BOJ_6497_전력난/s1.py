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

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])

    p = list(range(m+1))
    ans = 0
    for idx in range(n):
        x = edges[idx][0]
        y = edges[idx][1]
        cost = edges[idx][2]
        if find(x) != find(y):
            union(x, y)
        else:
            ans += cost
    print(ans)

