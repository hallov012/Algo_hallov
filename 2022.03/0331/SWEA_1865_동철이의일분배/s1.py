import sys
sys.stdin = open('input.txt')

def find(cnt, idx):
    global ans
    if cnt <= ans:
        return
    if idx == n:
        ans = max(ans, cnt)
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            find(cnt * (percent[idx][j] / 100), idx + 1)
            visited[j] = 0

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    percent = [list(map(float, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 0
    find(1, 0)
    ans *= 100
    print("#{} {:.6f}".format(tc, ans))
