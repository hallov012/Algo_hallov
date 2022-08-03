"""
dijkstra와 dp를 이용한 문제 풀이
"""
import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(start):
    # 포장한 도로의 수를 카운트하기 위한 이차원배열
    # row: 도시, column: 포장한 도로의 수
    dist = [[sys.maxsize] * (k+1) for _ in range(n+1)]
    q = []
    # heap에는 (d, start, cnt)의 형태로 담는다
    heapq.heappush(q, (0, start, 0))
    dist[start][0] = 0
    while q:
        d, now, cnt = heapq.heappop(q)
        if dist[now][cnt] < d:
            continue
        for next, cost in g[now]:
            # 현재 cnt에서 갈 수 있는 최소 시간을 갱신
            if dist[next][cnt] > d + cost:
                dist[next][cnt] = d + cost
                heapq.heappush(q, (dist[next][cnt], next, cnt))
            # 아직 도로를 더 포장할 수 있고, 포장했을 경우 시간이 현재 저장된 시간보다 짧아진다면 도로를 포장해본다
            if cnt < k and dist[next][cnt+1] > d:
                dist[next][cnt+1] = d
                heapq.heappush(q, (d, next, cnt+1))
    return dist

input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

dist = dijkstra(1)
print(min(dist[n]))
