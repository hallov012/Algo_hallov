import sys
from collections import deque
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            visited = [[False] * m for _ in range(n)]
            visited[i][j] = 1
            que =