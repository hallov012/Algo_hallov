import sys
from collections import defaultdict, deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            flag = True
            que = deque([(i, 1)])
            while que:
                now, color = que.popleft()
                if visited[now] and visited[now] != color:
                    flag = False
                    break
                visited[now] = color
                for next in g[now]:
                    if not visited[next]:
                        que.append((next, -color))
            if not flag:
                print("impossible")
                break
    else:
        print("possible")

