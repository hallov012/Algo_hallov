import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

def dijkstra():
    dist[0][0] = 0
    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        d, x, y = heapq.heappop(q)
        if dist[x][y] < d:
            continue
        if x == n-1 and y == n-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                temp = abs(arr[x][y]-arr[nx][ny])
                if dist[nx][ny] > max(d, temp):
                    dist[nx][ny] = max(d, temp)
                    heapq.heappush(q, (dist[nx][ny], nx, ny))

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dist = [[sys.maxsize] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dijkstra()
print(dist[-1][-1])
