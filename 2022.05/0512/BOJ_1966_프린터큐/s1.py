import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    orders = list(map(int, input().split()))
    que = deque([])
    for i in range(n):
        que.append((orders[i], i))
    orders.sort(reverse=True)
    ans = []
    while True:
        order, idx = que.popleft()
        if order == orders[0]:
            ans.append(idx)
            orders.pop(0)
            if idx == m:
                print(len(ans))
                break
        else:
            que.append((order, idx))


