import sys
sys.stdin = open('input.txt')

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    x, y = find_set(x), find_set(y)
    parent[y] = x

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    parent = list(range(n+1))
    for _ in range(m):
        x, y = map(int, input().split())
        union(x, y)
    for i in range(1, n+1):
        find_set(i)
    ans = len(set(parent)) - 1
    print(f'#{tc} {ans}')

