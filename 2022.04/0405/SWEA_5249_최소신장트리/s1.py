import sys
sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[y] = x

def kruskal():
    global ans
    edge_cnt = idx = 0
    while edge_cnt != V:
        x = edges[idx][0]
        y = edges[idx][1]
        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            ans += edges[idx][2]
        idx += 1

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    p = list(range(V+1))
    edges = sorted(edges, key=lambda x: x[2])
    ans = 0
    kruskal()
    print(f'#{tc} {ans}')
