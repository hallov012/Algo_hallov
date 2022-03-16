import sys
sys.stdin = open('input.txt')

n = int(input())
g = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

que = [1]
visited = [0] * (n + 1)
visited[1] = 1
while que:
    v = que.pop(0)
    for w in g[v]:
        if not visited[w]:
            que.append(w)
            visited[w] = 1
            ans[w] = v
for i in range(2, n + 1):
    print(ans[i])