import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
g_origin = [[True] * n for _ in range(n)]
flag = True
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or i == k or j == k:
                continue
            # 다른 곳을 경유해서 i => j가 가능하니까 직통 경로는 없어도 된다
            if g[i][j] == g[i][k] + g[k][j]:
                g_origin[i][j] = False
            # 뭔가 이상함 (플로이드워셜이 성립하지 않음)
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