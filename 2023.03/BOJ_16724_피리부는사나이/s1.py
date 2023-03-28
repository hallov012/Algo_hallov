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
    elif x < y:
        p[y] = x
    else:
        p[x] = y

input = sys.stdin.readline

n, m = map(int, input().split())
dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
arr = [list(input()) for _ in range(n)]
p = list(range(n*m))
for now in range(n*m):
    x = now // m
    y = now % m
    d = arr[x][y]
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    next = nx * m + ny
    if 0 <= next < n*m:
        union(now, next)
ans = 0
visited = [0] * (n*m)
for i in range(n*m):
    if not visited[find(p[i])]:
        visited[find(p[i])] = 1
        ans += 1
print(ans)