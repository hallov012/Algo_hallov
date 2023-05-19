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

T = int(input())
for _ in range(T):
    r, c = map(int, input().split())
    edges = []
    for i in range(r):
        row = list(map(int, input().split()))
        for j in range(c-1):
            num = c*i + j
            edges.append((num, num+1, row[j]))
    for i in range(r-1):
        row = list(map(int, input().split()))
        for j in range(c):
            num = c*i + j
            edges.append((num, num+c, row[j]))
    edges.sort(key=lambda x:x[2])
    n = r*c - 1
    edge_cnt = 0
    ans = 0
    p = list(range(r*c))
    for i in range(len(edges)):
        a, b, d = edges[i]
        if find(a) != find(b):
            union(a, b)
            ans += d
            edge_cnt += 1
        if edge_cnt == n:
            break
    print(ans)