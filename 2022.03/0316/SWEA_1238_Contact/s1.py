import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    e, start = map(int, input().split())
    temp = list(map(int, input().split()))
    n = max(temp)
    g = [[] for _ in range(n + 1)]
    for i in range(e//2):
        g[temp[2 * i]].append(temp[2 * i + 1])
    que = [start]
    visited = [0] * (n + 1)
    visited[start] = 1
    while que:
        v = que.pop(0)
        for w in g[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                que.append(w)
    for i in range(n, 0, -1):
        if visited[i] == max(visited):
            print(f'#{tc} {i}')
            break
