import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E, a, b = map(int, input().split())
    temp = list(map(int, input().split()))
    g = [[] for _ in range(V + 1)]
    for i in range(E):
        g[temp[2 * i]].append(temp[2 * i + 1])
    c = max(a, b)
    visited_cnt = V ** 2
    for i in range(V, 0, -1):
        cnt = 1
        visited = [0] * (V + 1)
        que = [i]
        visited[i] = 1
        while que:
            v = que.pop(0)
            for w in g[v]:
                if not visited[w]:
                    visited[w] = visited[v] + 1
                    que.append(w)
                    cnt += 1
        if visited[a] and visited[b]:
            if visited_cnt > visited[a] + visited[b]:
                visited_cnt = visited[a] + visited[b]
                ans = [i, cnt]

    print(f'#{tc}', *ans)



