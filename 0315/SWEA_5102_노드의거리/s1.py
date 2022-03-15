import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    g = [[] for _ in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    que = [S]
    visited[S] = 1
    while que:
        v = que.pop(0)
        if v == G:
            break
        for w in g[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                que.append(w)
    if not visited[G]:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {visited[G]-1}')