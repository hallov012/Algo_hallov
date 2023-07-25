import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(a, b):
    dist = [[sys.maxsize] * M for _ in range(N)]
    dist[a][b] = 0
    q = []
    heapq.heappush(q, (a, b, 0))
    while q:
        x, y, d = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and abs(arr[x][y] - arr[nx][ny]) <= T:
                next_d = d
                if arr[x][y] <= arr[nx][ny]:
                    next_d += 1
                else:
                    next_d += (arr[x][y] - arr[nx][ny]) ** 2
                if next_d < dist[nx][ny]:
                    dist[nx][ny] = next_d
                    heapq.heappush(q, (nx, ny, next_d))
    return dist

input = sys.stdin.readline

N, M, T, D = map(int, input().split())
arr = []
for _ in range(N):
    data = input().rstrip()
    line = []
    for j in range(M):
        num = ord(data[j])
        if ord(data[j]) <= 90:
            line.append(num-65)
        else:
            line.append(num-71)
    arr.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist = dijkstra(0, 0)
can_go = []
for i in range(N):
    for j in range(M):
        if dist[i][j] < D:
            heapq.heappush(can_go, (-1 * arr[i][j], i, j))

while can_go:
    d, x, y = heapq.heappop(can_go)
    return_dist = dijkstra(x, y)
    if dist[x][y] + return_dist[0][0] <= D:
        print(-d)
        exit()