"""
dist[i]에 k개의 공간을 만들어 값을 넣고 정렬한 후 마지막 값=1부터 i까지 k번째 최단 경로
이것만 명심하면 다른 다익스트라 문제와 같다.
"""
import sys, heapq
sys.stdin = open('input.txt')

def dijkjstra(start):
    dist = [[sys.maxsize] * k for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    dist[start][0] = 0
    while q:
        d, now = heapq.heappop(q)
        for b, c in g[now]:
            # k번째 경로를 구하는 것이므로 K까지만 구하면 된다
            # 제일 마지막 인덱스인 [k-1]에 경로를 저장하고 sort해주는 방법으로 k번째 최단거리 탐색
            if d + c < dist[b][k-1]:
                dist[b][k-1] = d + c
                dist[b].sort()
                heapq.heappush(q, (d+c, b))
    return dist

input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

dist = dijkjstra(1)
print(dist)
for i in range(1, n+1):
    if dist[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(dist[i][k-1])