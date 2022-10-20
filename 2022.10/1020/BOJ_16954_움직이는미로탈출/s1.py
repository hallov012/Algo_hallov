"""
벽이 없을 때는 일반적인 bfs를 사용해 최단거리로 목표지점에 도달하면 된다
하지만 벽이 있다면 벽의 위치 상태에 따라 기존에 방문했던 곳도 재방문 할 수 있으므로 visited를 초기화한다
"""
import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

arr = []
wall = set()
for i in range(8):
    line = list(input().rstrip())
    arr.append(line)
    for j in range(8):
        if arr[i][j] == '#':
            wall.add((i, j))

visited = set()
que = deque([(7, 0)])
flag = 0
dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
while que:
    for _ in range(len(que)):
        x, y = que.popleft()
        if (x, y) in wall:
            continue
        if (x, y) == (0, 7):
            flag = 1
            break
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if not (nx, ny) in wall and not (nx, ny) in visited:
                    visited.add((nx, ny))
                    que.append((nx, ny))
    if wall:
        visited = set()
    new_wall = set()
    for x, y in wall:
        if x < 7:
            new_wall.add((x+1, y))
    wall = new_wall
print(flag)

