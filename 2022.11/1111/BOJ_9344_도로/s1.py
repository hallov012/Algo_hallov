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

T = int(input())
for _ in range(T):
    n, m, s, e = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges.sort(key=lambda x:x[2])
    p = list(range(n+1))
    edge_cnt = 0
    flag = False
    for idx in range(m):
        x = edges[idx][0]
        y = edges[idx][1]
        if find(x) != find(y):
            union(x, y)
            edge_cnt += 1
            if (x, y) == (s, e) or (y, x) == (s, e):
                flag = True
                break
            if edge_cnt == n-1:
                break
    if flag:
        print("YES")
    else:
        print("NO")

