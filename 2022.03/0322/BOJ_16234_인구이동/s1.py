import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
time = 0
while 1:
    visited = [[0] * n for _ in range(n)]
    check = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                unite = [[i, j]]
                unite_population = population[i][j]
                visited[i][j] = 1
                que = deque([[i, j]])
                while que:
                    x, y = que.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and l <= abs(population[x][y] - population[nx][ny]) <= r:
                                visited[nx][ny] = 1
                                unite.append([nx, ny])
                                unite_population += population[nx][ny]
                                que.append([nx, ny])
                if len(unite) > 1:
                    for idx in unite:
                        population[idx[0]][idx[1]] = unite_population // len(unite)
                        check = True
    if not check:
        break
    time += 1

print(time)





