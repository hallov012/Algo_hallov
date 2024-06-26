import sys
sys.stdin = open('input.txt')

def find(x):
    if x == p[x]:
        return x
    p[x] = find(p[x])
    return p[x]

def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
direct = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

p = list(range(n * m))
for i in range(n * m):
    x = i // m
    y = i % m
    d = arr[x][y]
    nx = x + direct[d][0]
    ny = y + direct[d][1]
    next = nx * m + ny
    # 현재 위치와 다음으로 이동하는 위치를 이어주기
    if 0 <= next < n * m:
        union(i, next)

group = set()
for i in range(n * m):
    group.add(find(i))
print(len(group))