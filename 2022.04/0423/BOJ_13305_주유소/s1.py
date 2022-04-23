import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = min(cost[:-1])
min_idx = cost.index(min_cost)
idx = [min_idx]
i = min_idx
while i != 0:
    sub_min_cost = min(cost[:i])
    i = cost.index(sub_min_cost)
    idx.append(i)
ans = 0
idx.reverse()
for j in range(len(idx)):
    if j == len(idx)-1:
        ans += cost[j] * sum(distance[j:])
    else:
        ans += cost[j] * sum(distance[j: idx[j+1]])
print(ans)