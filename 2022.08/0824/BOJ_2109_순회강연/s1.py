import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: x[1])
ans = []
for i in range(n):
    p, d = data[i]
    heapq.heappush(ans, p)
    if len(ans) > d:
        heapq.heappop(ans)
print(sum(ans))
