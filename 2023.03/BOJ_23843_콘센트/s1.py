import sys, heapq
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
heap = [0] * m
for time in arr:
    c = heapq.heappop(heap)
    heapq.heappush(heap, time+c)
print(max(heap))
