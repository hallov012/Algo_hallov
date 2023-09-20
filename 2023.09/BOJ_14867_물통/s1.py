import sys
from collections import deque
sys.stdin = open('input.txt')

a, b, c, d = map(int, input().split())
visited = [[-1] * (b+1) for _ in range(a+1)]
visited[0][0] = 0
que = deque([(0, 0)])

while que:
    x, y = que.popleft()
    if (x, y) == (c, d):
        break
    # A 물통을 채우기, 비우기
    if visited[a][y] == -1:
        visited[a][y] = visited[x][y] + 1
        que.append((a, y))
    if visited[0][y] == -1:
        visited[0][y] = visited[x][y] + 1
        que.append((0, y))
    # B 물통 채우기, 비우기
    if visited[x][b] == -1:
        visited[x][b] = visited[x][y] + 1
        que.append((x, b))
    if visited[x][0] == -1:
        visited[x][0] = visited[x][y] + 1
        que.append((x, 0))
    # A => B, B => A 옮기기
    if x <= b-y:
        if visited[0][y+x] == -1:
            visited[0][y+x] = visited[x][y] + 1
            que.append((0, y+x))
    else:
        if visited[x-(b-y)][b] == -1:
            visited[x-(b-y)][b] = visited[x][y] + 1
            que.append((x-(b-y), b))
    if y <= a-x:
        if visited[x+y][0] == -1:
            visited[x+y][0] = visited[x][y] + 1
            que.append((x+y, 0))
    else:
        if visited[a][y-(a-x)] == -1:
            visited[a][y-(a-x)] = visited[x][y] + 1
            que.append((a, y-(a-x)))


print(visited[c][d])



