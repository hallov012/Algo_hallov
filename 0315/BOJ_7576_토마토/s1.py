import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tomatos = []
stop_change = []
ans = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomatos.append([i, j])
while 1:
    changes = []
    for tomato in tomatos:
        if tomato not in stop_change:
            keep_change = False
            x, y = tomato
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if box[nx][ny] == 0:
                        changes.append([nx, ny])
                        keep_change = True
            if not keep_change:
                stop_change.append(tomato)
    if changes:
        for change in changes:
            a, b = change
            box[a][b] = 1
            tomatos.append([a, b])
    else:
        break
    ans += 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            ans = -1
        break
print(ans)



