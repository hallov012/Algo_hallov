import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

q = int(input())
info = defaultdict(list)
ans = 0
for _ in range(q):
    data = list(map(str, input().split()))
    # 고릴라
    if data[0] == '1':
        name = data[1]
        for c in data[3:]:
            heapq.heappush(info[name], -int(c))
    elif data[0] == '2':
        name = data[1]
        num = int(data[2])
        if len(info[name]) <= num:
            ans += -sum(info[name])
            info[name] = []
        else:
            for _ in range(num):
                ans += -heapq.heappop(info[name])
print(ans)