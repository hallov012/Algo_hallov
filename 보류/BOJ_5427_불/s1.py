import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    visited = [[0] * w for _ in range(h)]
    fire = deque()
    que = deque()
    arr = []
    for i in range(h):
        line = list(input().rstrip())
        arr.append(line)
        for j in range(w):
            if line[j] == '@':
                que.append((i, j))
                arr[i][j] = 0
            if line[j] == '*':
                fire.append((i, j))
                visited[i][j] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = -1
    while que:
        new = deque()
        while que:
            x, y = que.popleft()
            if (x == h-1 or y == w-1 or x == 0 or y == 0) and arr[x][y] != "*":
                ans = arr[x][y] + 1
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if arr[nx][ny] == '.' and arr[x][y] != '*':
                        arr[nx][ny] = arr[x][y] + 1
                        new.append((nx, ny))
        que = new
        new_fire = deque()
        while fire:
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if not visited[nx][ny] and arr[nx][ny] != '#':
                        visited[nx][ny] = 1
                        arr[nx][ny] = '*'
                        new_fire.append((nx, ny))
        fire = new_fire

    if ans != -1:
        print(ans)
    else:
        print("IMPOSSIBLE")