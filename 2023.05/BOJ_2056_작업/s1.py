import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
dp = [0] * (n+1)
for i in range(1, n+1):
    time, cnt, *lst = map(int, input().split())
    dp[i] = time
    for x in lst:
        g[i].append(x)

for i in range(1, n+1):
    temp = 0
    for j in g[i]:
        temp = max(temp, dp[j])
    dp[i] += temp

print(max(dp))
