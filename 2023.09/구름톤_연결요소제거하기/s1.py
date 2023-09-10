import sys
from collections import deque
sys.stdin = open('input.txt')

def remove_char():
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] != '.':
                visited[i][j] = True
                tmp = [(i, j)]
                que = deque([(i, j)])
                char = arr[i][j]
                while que:
                    x, y = que.popleft()
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == char and not visited[nx][ny]:
                                visited[nx][ny] = True
                                que.append((nx, ny))
                                tmp.append((nx, ny))
                if len(tmp) >= k:
                    for x, y in tmp:
                        arr[x][y] = '.'



n, k, q = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(q):
    a, b, d = map(str, input().split())
    a, b = int(a)-1, int(b)-1
    arr[a][b] = d
    remove_char()

for line in arr:
    print(''.join(line))


