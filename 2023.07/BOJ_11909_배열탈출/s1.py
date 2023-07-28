import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(a, b):
    dist = [[sys.maxsize] * n for _ in range(n)]
    dist[a][b] = 0
    q = []
    heapq.heappush(q, (0, a, b))
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_d = d
                if arr[x][y] <= arr[nx][ny]:
                    next_d += arr[nx][ny] - arr[x][y] + 1
                if dist[nx][ny] > next_d:
                    dist[nx][ny] = next_d
                    heapq.heappush(q, (next_d, nx, ny))
    return dist

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0]
dy = [0, 1]
dist = dijkstra(0, 0)
print(dist[n-1][n-1])