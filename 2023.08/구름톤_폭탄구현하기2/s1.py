import sys
sys.stdin = open('input.txt')

def boom(a, b):
    if 0 <= a < n and 0 <= b < n:
        if arr[a][b] == '0':
            cnt[a][b] += 1
        elif arr[a][b] == '@':
            cnt[a][b] += 2
    return

n, k = map(int, input().split())
arr = [input().split() for _ in range(n)]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
cnt = [[0] * n for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]
        boom(nx, ny)

ans = 0
for line in cnt:
    ans = max(ans, max(line))

print(ans)
