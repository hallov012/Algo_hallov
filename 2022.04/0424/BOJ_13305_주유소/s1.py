import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = cost[0]
ans = 0
for i in range(n-1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    ans += min_cost * distance[i]
print(ans)