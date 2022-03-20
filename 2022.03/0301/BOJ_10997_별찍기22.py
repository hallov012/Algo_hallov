n = int(input())

if n == 1:
    print('*')
    exit(0)

w, h = 4 * (n - 1) + 1, 4 * n - 1
arr = [[' '] * w for _ in range(h)]
arr[0] = arr[-1] = ['*'] * w
for i in range(1, h-1):
    arr[i][0] = '*'

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
x, y = -1, -1
i = 0
cnt = 0
while cnt < n:
    if i == 0:   # 위로 이동
        while arr[x + dx[i] - 1][y + dy[i]] != '*':
            x += dx[i]
            y += dy[i]
            arr[x][y] = '*'
    elif i == 1:     # 왼쪽 이동
        while arr[x + dx[i]][y + dy[i] - 1] != '*':
            x += dx[i]
            y += dy[i]
            arr[x][y] = '*'
    elif i == 2:
        while arr[x + dx[i] + 1][y + dy[i]] != '*':
            x += dx[i]
            y += dy[i]
            arr[x][y] = '*'
    else:
        while arr[x + dx[i]][y + dy[i] + 1] != '*':
            x += dx[i]
            y += dy[i]
            arr[x][y] = '*'
    i += 1
    if i == 4:
        i = i % 4
        cnt += 1

for i in range(h):
    if i == 1:
        print(arr[i][0])
    else:
        a = ''.join(arr[i])
        print(a)

