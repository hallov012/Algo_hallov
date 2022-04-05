import sys
sys.stdin = open('input.txt')

def dfs(idx, w_cnt, value):
    global ans
    if w_cnt == k:
        ans = max(value, ans)
        return
    if idx == n:
        ans = max(value, ans)
        return
    if w_cnt + subjects[idx][0] <= k:
        dfs(idx + 1, w_cnt + subjects[idx][0], value + subjects[idx][1])
    dfs(idx+1, w_cnt, value)

input = sys.stdin.readline

n, k = map(int, input().split())
subjects = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 0, 0)
print(ans)