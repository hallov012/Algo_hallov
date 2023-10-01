import sys, heapq
sys.stdin = open('input.txt')

def dijkstra(a, b):
    dist = [[sys.maxsize] * w for _ in range(h)]
    dist[a][b] = 0
    q = []
    heapq.heappush(q, (0, a, b))
    while q:
        d, x, y = heapq.heappop(q)
        if x in (0, h-1) or y in (0, w-1):
            return d
        if dist[x][y] < d:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                tmp = d + time[arr[nx][ny]]
                if dist[nx][ny] > tmp:
                    dist[nx][ny] = tmp
                    heapq.heappush(q, (tmp, nx, ny))
    return -1

input = sys.stdin.readline

T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    k, w, h = map(int, input().split())
    time = {}
    for _ in range(k):
        name, t = map(str, input().split())
        time[name] = int(t)
    time['E'] = 0
    arr = []
    sx, sy = 0, 0
    for i in range(h):
        row = input().rstrip()
        for j in range(w):
            if row[j] == 'E':
                sx, sy = i, j
        arr.append(row)

    ans = dijkstra(sx, sy)
    print(ans)