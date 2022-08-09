import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
virus = []
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
    for j in range(n):
        if line[j]:
            virus.append((line[j], i, j))
s, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus.sort()
que = deque(virus)
cnt = 0
while que:
    if cnt == s:
        break
    for _ in range(len(que)):
        v, x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not arr[nx][ny]:
                    arr[nx][ny] = v
                    que.append((v, nx, ny))
    cnt += 1

print(arr[X-1][Y-1])