import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
heap = [(0, 0)]
cnt = [0]
for s, e in arr:
    temp = []
    while heap:
        time, idx = heapq.heappop(heap)
        if time <= s:
            heapq.heappush(temp, (idx, time))
        else:
            heapq.heappush(heap, (time, idx))
            break
    if temp:
        idx, time = heapq.heappop(temp)
        heapq.heappush(heap, (e, idx))
        cnt[idx] += 1
        for i, t in temp:
            heapq.heappush(heap, (t, i))
    else:
        heapq.heappush(heap, (e, len(heap)))
        cnt.append(1)
print(len(heap))
print(*cnt)