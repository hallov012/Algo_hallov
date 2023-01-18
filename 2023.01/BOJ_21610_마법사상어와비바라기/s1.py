import sys
from collections import deque
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
move = [list(map(int, input().split())) for _ in range(m)]
cloud = [[0] * n for _ in range(n)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
que = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for x, y in cloud:
    cloud[x][y] = 1
for d, s in move:
    d -= 1
    new_que = []
    for x, y in que:
        nx = ((x + dx[d]) * s) % n
        ny = ((y + dy[d]) * s) % n
        arr[nx][ny] += 1
        for
