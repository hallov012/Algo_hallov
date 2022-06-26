import sys, heapq
from collections import deque, defaultdict
sys.stdin = open('input.txt')

def dijkstra():
    dist = [sys.maxsize] * n
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for v, p in g[now]:
            if d + p < dist[v]:
                dist[v] = d + p
                heapq.heappush(q, (dist[v], v))
    return dist

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if not n and not m:
        break
    s, d = map(int, input().split())
    g = [[] for _ in range(n)]
    g_reverse = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, input().split())
        g[u].append((v, p))
        g_reverse[v].append((u, p))
    dist = dijkstra()

    remove_dic = defaultdict(list)
    que = deque()
    que.append(d)
    while que:
        v = que.popleft()
        if v == s:
            continue
        for w, p in g_reverse[v]:
            # 최단경로일 경우, 그 경로를 remove_dic에 넣어준다
            if dist[w] + p == dist[v]:
                if (v, p) not in remove_dic[w]:
                    remove_dic[w].append((v, p))
                    que.append(w)
    # 최단 경로를 삭제
    for key in remove_dic.keys():
        for w, p in remove_dic[key]:
            g[key].remove((w, p))

    new_dist = dijkstra()
    if new_dist[d] == sys.maxsize:
        print(-1)
    else:
        print(new_dist[d])

