import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    buildings = [0] + list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    inDegree = [0] * (n+1)
    dp = [0] * (n+1)

    for i in range(k):
        x, y = map(int, input().split())
        g[x].append(y)
        inDegree[y] += 1

    que = deque()
    for i in range(1, n+1):
        if not inDegree[i]:
            que.append(i)
            dp[i] = buildings[i]

    while que:
        x = que.popleft()
        for y in g[x]:
            inDegree[y] -= 1
            # 만약 g[x1] = [y], g[x2] = [y] 일 때, x1과 x2 모두 건설이 끝나야 y로 진입할 수 있으므로 max값을 dp로 새로 지
            dp[y] = max(dp[x]+buildings[y], dp[y])
            if not inDegree[y]:
                que.append(y)
    w = int(input())
    print(dp[w])

