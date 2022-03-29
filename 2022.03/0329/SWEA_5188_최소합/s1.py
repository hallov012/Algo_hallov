import sys
sys.stdin = open('input.txt')

def min_sum(x, y, cnt):
    global ans
    if cnt > ans:
        return
    if x == n-1 and y == n-1:
        ans = min(ans, cnt)
        return
    else:
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    min_sum(nx, ny, cnt + data[nx][ny])
                    visited[nx][ny] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    dx = [1, 0]
    dy = [0, 1]
    ans = 10 * (n ** 2)
    min_sum(0, 0, data[0][0])
    print(f'#{tc} {ans}')