import sys
sys.stdin = open('input.txt')

def dfs(temp):
    x, y, z = temp
    # z: 0 가로 1 세로 2 대각선
    global cnt
    if x == n-1 and y == n-1:
        cnt += 1
        return
    # 대각선 이동
    if x+1 < n and y+1 < n:
        if not arr[x+1][y+1] and not arr[x+1][y] and not arr[x][y+1]:
            dfs((x+1, y+1, 2))
    # 가로 이동
    if z == 0 or z == 2:
        if y+1 < n:
            if not arr[x][y+1]:
                dfs((x, y+1, 0))
    # 세로 이동
    if z == 1 or z == 2:
        if x+1 < n:
            if not arr[x+1][y]:
                dfs((x+1, y, 1))

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
dfs((0, 1, 0))
print(cnt)