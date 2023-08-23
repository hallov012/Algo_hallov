import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = 0

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            continue
        cnt = 0
        for d in range(8):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                cnt += 1
        if cnt == k:
            ans += 1
print(ans)