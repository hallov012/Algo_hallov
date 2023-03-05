import sys, heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(arr, (s, e))

c_lst = [0]
cnt = [0]
while arr:
    s, e = heapq.heappop(arr)
    for i in range(len(c_lst)):
        if c_lst[i] <= s:
            c_lst[i] = e
            cnt[i] += 1
            break
    else:
        c_lst.append(e)
        cnt.append(1)
print(len(c_lst))
print(*cnt)