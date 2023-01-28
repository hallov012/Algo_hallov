import sys
sys.stdin = open('input.txt')

def dfs(idx):
    global ans
    if idx == n:
        cnt = 0
        for s, w in eggs:
            if s <= 0:
                cnt += 1
        ans = max(ans, cnt)
        return
    if eggs[idx][0] <= 0:
        dfs(idx+1)
    else:
        flag = True
        for i in range(n):
            if idx != i and eggs[i][0] > 0:
                flag = False
                eggs[idx][0] -= eggs[i][1]
                eggs[i][0] -= eggs[idx][1]
                dfs(idx+1)
                eggs[idx][0] += eggs[i][1]
                eggs[i][0] += eggs[idx][1]
        if flag:
            dfs(n)

input = sys.stdin.readline

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0)
print(ans)
