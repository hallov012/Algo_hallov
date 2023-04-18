import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

w, h = map(int, input().split())
arr = []
laser = []
for i in range(h):
    line = list(input())
    for j in range(w):
        if line[j] == 'C':
            laser.append((i, j))
    arr.append(line)
start = (laser[0][0], laser[0][1], -5, -1)
ans = sys.maxsize
end = laser[1]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
que = deque()
visited = [[[sys.maxsize] * w for _ in range(h)] for _ in range(4)]
que.append(start)

while que:
    x, y, d, cnt = que.popleft()
    if x == end[0] and y == end[1]:
        ans = min(ans, cnt)
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        val = cnt + 1 if d != i else cnt
        if 0 <= nx < h and 0 <= ny < w:
            if arr[nx][ny] != '*' and abs(d-i) != 2:
                if visited[i][nx][ny] > val:
                    que.append((nx, ny, i, val))
                    visited[i][nx][ny] = val
print(ans)