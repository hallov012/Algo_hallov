import sys
sys.stdin = open('input.txt')

def find(cnt, idx):
    global ans
    if cnt >= ans:
        return
    if idx == n:
        ans = min(ans, cnt)
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            find(cnt + v[idx][j], idx + 1)
            visited[j] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 99 * n
    find(0, 0)
    print(f'#{tc} {ans}')