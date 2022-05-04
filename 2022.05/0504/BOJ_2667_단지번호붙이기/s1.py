import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if data[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            cnt += 1
                            que.append((nx, ny))
            ans.append(cnt)
ans.sort()
print(len(ans))
if ans:
    for num in ans:
        print(num)




