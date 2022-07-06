import sys, heapq
sys.stdin = open('input.txt')

T = int(input())

def dijkstra(start):
    dp = [[sys.maxsize] * (n+1) for _ in range(m+1)]
    q = []
    heapq.heappush(q, (0, 0, start))
    dp[start][0] = 0
    while q:
        dist, cost, now = heapq.heappop(q)
        if dist > dp[cost][now]:
            continue
        for v, c, d in g[now]:
            temp_dist = dist + d
            temp_cost = cost + c
            if temp_cost <= m and temp_dist < dp[temp_cost][v]:
                for i in range(temp_cost, m+1):
                    # 해당 금액에서 dist가 더 적게 필요한 것이므로 갱신
                    if dp[i][v] > temp_dist:
                        dp[i][v] = temp_dist
                    else:
                        break
                heapq.heappush(q, (temp_dist, temp_cost, v))
    return dp[m][n]

input = sys.stdin.readline

for tc in range(T):
    n, m, k = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        g[u].append((v, c, d))
    ans = dijkstra(1)
    if ans == sys.maxsize:
        print('Poor KCM')
    else:
        print(ans)