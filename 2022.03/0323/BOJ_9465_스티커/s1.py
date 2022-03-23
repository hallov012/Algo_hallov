import sys, copy
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dfs(data, cnt, score):
    global ans
    now_data = copy.deepcopy(data)
    if cnt == n * 2:
        ans = max(ans, score)
        return
    for i in range(2):
        for j in range(n):
            c = 0
            s = 0
            if now_data[i][j] >= 0:
                c += 1
                s = now_data[i][j]
                now_data[i][j] = -1
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < 2 and 0 <= ny < n:
                        if now_data[nx][ny] >= 0:
                            c += 1
                            now_data[nx][ny] = -1
                dfs(now_data, cnt+c, score+s)
                now_data = copy.deepcopy(data)

T = int(input())

for tc in range(T):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(2)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    ans = 0
    dfs(data, 0, 0)
    print(ans)