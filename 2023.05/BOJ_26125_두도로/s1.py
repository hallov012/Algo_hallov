import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, s, t = map(int, input().split())
g = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    g[i][i] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = min(g[u][v], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

q = int(input())
for _ in range(q):
    a1, b1, c1, a2, b2, c2 = map(int, input().split())
    # a1 => b1으로 가는 경로를 추가하는 경우 g[s][a1] + c1 + g[b1][t]
    # a2 => b2으로 가는 경로를 추가하는 경우 g[s][a2] + c2 + g[b2][t]
    # 그럼 둘 다 사용하는 경우는..?
    # s => a1 => b2 => a2 => b2 => t의 경우 g[s][a1] + c1 + g[b1][a2] + c2 + g[b2][t]
    # s => a2 => b2 => a1 => b1 => t
    ans = min(g[s][t], g[s][a1] + c1 + g[b1][t], g[s][a2] + c2 + g[b2][t],
              g[s][a1] + c1 + g[b1][a2] + c2 + g[b2][t], g[s][a2] + c2 + g[b2][a1] + c1 + g[b1][t])
    if ans == sys.maxsize:
        print(-1)
    else:
        print(ans)

