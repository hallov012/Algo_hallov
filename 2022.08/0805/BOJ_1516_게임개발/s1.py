import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
time = [0] * (n+1)
for i in range(1, n+1):
    line = list(map(int, input().split()))[:-1]
    time[i] = line[0]
    for j in range(1, len(line)):
        g[line[j]].append(i)
        in_degree[i] += 1

ans = [0] * (n+1)
que = deque()
for i in range(1, n+1):
    if not in_degree[i]:
        que.append(i)

while que:
    a = que.popleft()
    ans[a] += time[a]
    for b in g[a]:
        in_degree[b] -= 1
        ans[b] = max(ans[b], ans[a])
        if not in_degree[b]:
            que.append(b)

for i in range(1, n+1):
    print(ans[i])