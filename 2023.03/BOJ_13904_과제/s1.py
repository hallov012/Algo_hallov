import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
assignments = []
for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(assignments, (-w, d))
ans = [0] * 1001
while assignments:
    w, d = heapq.heappop(assignments)
    w *= -1
    for i in range(d-1, -1, -1):
        if not ans[i]:
            ans[i] = w
            break

print(sum(ans))






