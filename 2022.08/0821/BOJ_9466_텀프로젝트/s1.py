import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(now):
    global ans
    visited[now] = 1
    members.append(now)
    next = data[now]
    if visited[next]:
        if next in members:
            ans += len(members) - members.index(next)
        return
    else:
        dfs(next)

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            members = []
            dfs(i)

    print(n - ans)