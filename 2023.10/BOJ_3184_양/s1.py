import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

o_ans = v_ans = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and arr[i][j] != '#':
            o_cnt = v_cnt = 0
            visited[i][j] = True
            que = deque([(i, j)])
            while que:
                x, y = que.popleft()
                if arr[x][y] == 'o':
                    o_cnt += 1
                elif arr[x][y] == 'v':
                    v_cnt += 1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        if arr[nx][ny] != '#' and not visited[nx][ny]:
                            visited[nx][ny] = True
                            que.append((nx, ny))
            if o_cnt > v_cnt:
                o_ans += o_cnt
            else:
                v_ans += v_cnt

print(o_ans, v_ans)

