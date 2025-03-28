import sys
from collections import deque
sys.stdin = open('input.txt')

n, w, l = map(int, input().split())
trucks = deque(list(map(int, input().split())))

que = deque()
t = 1
total = 0
while trucks:
    # 이미 있는 트럭이 빠져나갈 수 있는지 체크
    if que:
        a, b = que[0]
        if (b + w) > t:
            t = b + w
        que.popleft()
        total -= a
    while trucks and total + trucks[0] <= l and len(que) < w:
        total += trucks[0]
        que.append((trucks[0], t))
        trucks.popleft()
        t += 1
print(t + w - 1)
