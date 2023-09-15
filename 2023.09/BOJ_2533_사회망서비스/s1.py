import sys
from collections import defaultdict
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    dp[v][0] = 1
    for w in tree[v]:
        if not visited[w]:
            dfs(w)
            dp[v][0] += min(dp[w][0], dp[w][1])
            dp[v][1] += dp[w][0]

input = sys.stdin.readline

n = int(input())
tree = defaultdict(list)
# k가 얼리어답터일 때 dp[k][0], k가 얼리어답터가 아닐 때 dp[k][1]에 값을 갱신
dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

print(min(dp[1]))