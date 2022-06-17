import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
# 북, 동, 남, 서 => 왼쪽으로 돌 때, 0, 3, 2, 1 순서로 방향이 전환되어야 한다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 1
data[x][y] = -1 # 청소한 구역은 -1로 변경한다
while True:
    flag = False
    for _ in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 0:
                ans += 1
                data[nx][ny] = -1
                x = nx
                y = ny
                flag = True
                break
    if not flag:
        nx = x - dx[d]
        ny = y - dy[d]
        if data[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
print(ans)

