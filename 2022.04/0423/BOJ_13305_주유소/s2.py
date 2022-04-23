import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
distance = [0] + list(map(int, input().split()))
cost = list(map(int, input().split()))

for i in range(1, len(distance)):
    distance[i] += distance[i-1]
min_cost = 200000
idx = []
for i in range(len(cost)-1):
    if cost[i] < min_cost:
        idx.append(i)
        min_cost = cost[i]
ans = 0
for j in range(len(idx)):
    if j == len(idx)-1:
        ans += cost[j] * (distance[-1] - distance[j])
    else:
        ans += cost[j] * (distance[idx[j+1]] - distance[j])
print(ans)