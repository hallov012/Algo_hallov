import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1
    num, i = 2, 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    nx, ny = 0, 0
    while num <= n ** 2:
        while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and not arr[nx+dx[i]][ny+dy[i]]:
            nx += dx[i]
            ny += dy[i]
            arr[nx][ny] = num
            num += 1
        i += 1
        if i == 4:
            i = i % 4
    print(f'#{tc}')
    for i in range(n):
        print(*arr[i])

