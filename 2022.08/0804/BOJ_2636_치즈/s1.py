import sys
from collections import deque
sys.stdin = open('input.txt')

def air():
    air_arr = [[0] * m for _ in range(n)]
    air_arr[0][0] = 1
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not air_arr[nx][ny] and not arr[nx][ny]:
                    air_arr[nx][ny] = 1
                    que.append((nx, ny))
    return air_arr

def melt():
    air_arr = air()
    melt_lst = []
    for x in range(n):
        for y in range(m):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and air_arr[nx][ny]:
                        melt_lst.append((x, y))
                        break
    for a, b in melt_lst:
        arr[a][b] = 0

def done():
    cnt = 0
    for line in arr:
        cnt += sum(line)
    return cnt

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
left_lst = [done()]
while True:
    melt()
    ans += 1
    left = done()
    if left:
        left_lst.append(left)
    else:
        break

print(ans)
print(left_lst[-1])