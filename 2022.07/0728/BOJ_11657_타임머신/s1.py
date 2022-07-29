"""
벨만 포드 알고리즘 사용
"""
import sys
sys.stdin = open('input.txt')

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            if dist[now] != sys.maxsize and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n-1:
                    return True
    return False

input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist = [sys.maxsize] * (n+1)
if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == sys.maxsize:
            print(-1)
        else:
            print(dist[i])