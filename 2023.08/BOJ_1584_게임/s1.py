import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(a, b):
    dist = [[sys.maxsize] * 501 for _ in range(501)]
    dist[0][0] = 0
    q = []
    heapq.heappush(q, (0, a, b))
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 501 and 0 <= ny < 501:
                temp = d
                if arr[nx][ny] == 2:
                    continue
                elif arr[nx][ny] == 1:
                    temp += 1
                if temp < dist[nx][ny]:
                    dist[nx][ny] = temp
                    heapq.heappush(q, (temp, nx, ny))
    return dist

input = sys.stdin.readline

arr = [[0] * 501 for _ in range(501)]
# 위험한 구역 => 1
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] = 1

# 죽음의 구역 => 2
m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arr[i][j] = 2

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist = dijkstra(0, 0)
print(dist[500][500] if dist[500][500] != sys.maxsize else -1)