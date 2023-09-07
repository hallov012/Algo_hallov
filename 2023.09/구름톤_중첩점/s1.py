import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [[[0] * 2 for _ in range(n)] for _ in range(n)]
dirt = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
for _ in range(m):
    x, y, d = input().split()
    x = int(x) - 1
    y = int(y) - 1
    if d in 'RL':
        d_type = 0
    else:
        d_type = 1
    while 0 <= x < n and 0 <= y < n:
        arr[x][y][d_type] += 1
        x += dirt[d][0]
        y += dirt[d][1]

ans = 0
for i in range(n):
    for j in range(n):
        ans += arr[i][j][0] * arr[i][j][1]

print(ans)