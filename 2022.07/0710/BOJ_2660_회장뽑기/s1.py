import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
dist = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

min_cnt = sys.maxsize
candidate = []
for i in range(1, n+1):
    if min_cnt > max(dist[i][1:]):
        min_cnt = max(dist[i][1:])
        candidate = [i]
    elif min_cnt == max(dist[i][1:]):
        candidate.append(i)

print(min_cnt, len(candidate))
print(*candidate)
