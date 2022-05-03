import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

k = int(input())
for tc in range(k):
    v, e = map(int, input().split())
    visited = [0] * (v+1)
    g = defaultdict(list)
    for _ in range(e):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)

    ans = True
    # 그래프가 모두 연결되어있지 않을수도 있기 때문에 모든 edge에 dfs를 한번은 스타트해줘야한다
    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            que = deque([(i, 1)])
            while que:
                s, flag = que.popleft()
                for e in g[s]:
                    if visited[e] == 0:
                        visited[e] = -flag
                        que.append((e, -flag))
                    elif visited[e] == flag:
                        ans = False
                        break

    if ans:
        print('YES')
    else:
        print('NO')
