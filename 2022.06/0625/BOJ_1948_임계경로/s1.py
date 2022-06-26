import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
g_reverse = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    indegree[b] += 1
    g_reverse[b].append((a, c))
s, e = map(int, input().split())

# 각 도시로 이동하는 최장거리를 담는 dp 생성
# 문제에서 출발도시는 항상 indegree가 0이라고 했으니 출발 도시에서 각 도시로 가는 최장거리를 구하는 것
que = deque()
dp = [0] * (n+1)
for i in range(1, n+1):
    if not indegree[i]:
        que.append((i, 0))
while que:
    now, cost = que.popleft()
    for b, c in g[now]:
        indegree[b] -= 1
        dp[b] = max(dp[b], dp[now] + c)
        if not indegree[b]:
            que.append((b, cost + c))

# 최장거리를 지날 때 지나는 도로의 수를 count => 경로를 edges에 저장한다
edges = set()
q = deque()
q.append((e, 0))
while q:
    now, cost = q.popleft()
    for a, c in g_reverse[now]:
        # 최장경로를 따라 가는 경우 edges에 add 한다
        if dp[now] == dp[a] + c and (a, now) not in edges:
            edges.add((a, now))
            q.append((a, cost + c))
print(dp[e])
print(len(edges))

