import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(a, b):
    dist = [[sys.maxsize] * m for _ in range(n)]
    q = []
    dist[a][b] = 0
    heapq.heappush(q, (0, a, b))
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                next_d = d
                if arr[nx][ny] == '1' or arr[nx][ny] == '#':
                    next_d += 1
                if next_d < dist[nx][ny]:
                    dist[nx][ny] = next_d
                    heapq.heappush(q, (next_d, nx, ny))
    return dist

input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
arr = [input().rstrip() for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dist = dijkstra(x1, y1)
print(dist[x2][y2])