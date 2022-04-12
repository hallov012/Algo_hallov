import sys
sys.stdin = open('input.txt')

def dfs(cnt, x, y, user_cnt):
    global ans
    if user_cnt + (4-cnt)*max_user <= ans:
        return
    if cnt == 4:
        ans = max(ans, user_cnt)
        return
    case = y % 2
    dx, dy = dx_lst[case], dy_lst[case]
    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(cnt+1, nx, ny, user_cnt + users[nx][ny])
                dfs(cnt+1, x, y, user_cnt + users[nx][ny])
                visited[nx][ny] = 0

T = int(input())

for tc in range(1, T+1):
    w, h = map(int, input().split())
    users = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    dx_lst = [(-1, -1, -1, 0, 0, 1), (-1, 0, 0, 1, 1, 1)]
    dy_lst = [(-1, 0, 1, -1, 1, 0), (0, -1, 1, -1, 0, 1)]
    max_user = 0
    for line in users:
        max_user = max(max_user, max(line))
    for i in range(h):
        for j in range(w):
            visited = [[0] * w for _ in range(h)]
            visited[i][j] = 1
            dfs(1, i, j, users[i][j])
    print(f'#{tc} {ans**2}')
