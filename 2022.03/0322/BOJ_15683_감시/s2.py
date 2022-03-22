import sys
import copy

sys.stdin = open('input.txt')

input = sys.stdin.readline

def check(x, y, directions, tmp):
    for d in directions:
        nx = x
        ny = y
        while 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < m:
            nx += dx[d]
            ny += dy[d]
            if tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break

def dfs(data, done):
    global ans
    temp = copy.deepcopy(data)
    if done == k:
        cnt = 0
        for i in range(n):
            cnt += temp[i].count(0)
        ans = min(ans, cnt)
        return
    x, y, cctv_num = cctv_lst[done]
    for i in range(len(cctv[cctv_num])):
        check(x, y, cctv[cctv_num][i], temp)
        dfs(temp, done + 1)
        temp = copy.deepcopy(data)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = n * m
dx = [-1, 0, 1, 0]  # 상 좌 하 우
dy = [0, -1, 0, 1]
cctv = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 3], [3, 2], [2, 1], [1, 0]],
        [[0, 3, 2], [3, 2, 1], [2, 1, 0], [1, 0, 3]], [[0, 1, 2, 3]]]
k = 0
cctv_lst = []
for r in range(n):
    for c in range(m):
        if arr[r][c] != 0 and arr[r][c] != 6:
            cctv_lst.append([r, c, arr[r][c]])
            k += 1

ans = n * m
dfs(arr, 0)
print(ans)
