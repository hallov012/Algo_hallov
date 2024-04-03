import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

"""
두 동전이 같이 이동
둘 중 하나만 떨어짐 
"""

n, m = map(int, input().split())
arr = []
visited = [[0] * m for _ in range(n)]
coin = []

for i in range(n):
    row = input().rstrip()
    arr.append(row)
    for j in range(m):
        if row[j] == 'o':
            coin.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 0, 1: 첫번째 코인 & 2, 3: 두번째 코인
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
(a, b), (c, d) = coin
visited[a][b][c][d] = 1

que = deque()
que.append((a, b, c, d))

t = 0
while que and t < 10:
    t += 1
    k = len(que)
    for _ in range(k):
        x, y, p, q = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            np = p + dx[i]
            nq = q + dy[i]

            xy_in, pq_in = 0, 0
            if 0 <= nx < n and 0 <= ny < m:
                xy_in = 1
                if arr[nx][ny] == '#':
                    nx, ny = x, y
            if 0 <= np < n and 0 <= nq < m:
                pq_in = 1
                if arr[np][nq] == '#':
                    np, nq = p, q

            if xy_in + pq_in == 1:
                print(t)
                exit()

            elif xy_in + pq_in == 2 and not visited[nx][ny][np][nq]:
                visited[nx][ny][np][nq] = 1
                que.append((nx, ny, np, nq))

print(-1)



