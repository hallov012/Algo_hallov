import sys
sys.stdin = open('input.txt')

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for now in range(1, n+1):
            for next, cost in edges[now]:
                if dist[now] != -sys.maxsize and dist[next] < dist[now] + cost:
                    dist[next] = dist[now] + cost
                    path[next] = now
                    if i == n-1:
                        dist[next] = sys.maxsize

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

dist = [-sys.maxsize] * (n+1)
path = [0] * (n+1)

bellman_ford(1)

if dist[n] == sys.maxsize:
    print(-1)
else:
    now = n
    ans = []
    while now != 1:
        ans.append(now)
        now = path[now]
    ans.append(now)
    ans.reverse()
    print(*ans)