import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
g_origin = [[1] * n for _ in range(n)]
flag = True
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 무조건 같게 나올 수 밖에 없는 구간들은 제외
            if i == j or i == k or j == k:
                continue
            if g[i][j] == g[i][k] + g[k][j]:
                g_origin[i][j] = 0
            elif g[i][j] > g[i][k] + g[k][j]:
                flag = False
                break
if not flag:
    print(-1)
else:
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if g_origin[i][j]:
                ans += g[i][j]
    print(ans)
