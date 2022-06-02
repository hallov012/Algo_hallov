import sys
sys.stdin = open('input.txt')

def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if not check[ord(data[nx][ny])-65]:
                check[ord(data[nx][ny])-65] = 1
                dfs(nx, ny, cnt+1)
                check[ord(data[nx][ny])-65] = 0

input = sys.stdin.readline

r, c = map(int, input().split())
data = [input() for _ in range(r)]
check = [0] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check[ord(data[0][0])-65] = 1
ans = 1
dfs(0, 0, 1)
print(ans)




