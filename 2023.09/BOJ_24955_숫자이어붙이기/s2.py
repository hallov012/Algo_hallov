import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, q = map(int, input().split())
a_lst = [''] + input().split()
g = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

m = 1000000007
for _ in range(q):
    x, y = map(int, input().split())
    visited = [False] * (n+1)
    visited[x] = True
    que = deque([(x, str(a_lst[x]))])
    while que:
        now, tmp = que.popleft()
        if now == y:
            print(int(tmp) % m)
            break
        for next in g[now]:
            if not visited[next]:
                visited[next] = True
                new_tmp = str(int(tmp + a_lst[next]) % m)
                que.append((next, new_tmp))
