import sys
from collections import deque
sys.stdin = open('input.txt')

n, q, c = map(int, input().split())
cap = [0] + list(map(int, input().split()))

# 최근에 방문한 순서로 que에 넣을 예정
back = deque()
front = deque()
now = -1
cnt = 0

for _ in range(q):
    input_data = input().split()
    command = input_data[0]
    if command == 'B':
        if back:
            front.appendleft(now)
            now = back.popleft()
    elif command == 'F':
        if front:
            back.appendleft(now)
            now = front.popleft()
    elif command == 'A':
        p = int(input_data[1])
        # front 비우기
        while front:
            x = front.pop()
            cnt -= cap[x]
        # 첫 접속이 아닌 경우만 뒤로가기 추가
        if now != -1:
            back.appendleft(now)
        now = p
        cnt += cap[p]
        # 만약 용량이 부족한 경우는 뒤로가기에서 페이지 삭제
        while cnt >= c:
            d_p = back.pop()
            cnt -= cap[d_p]
    else:
        l = len(back)
        last = -1
        for _ in range(l):
            x = back.popleft()
            # 이전에 나왔던 페이지와 같으면 삭제
            if x == last:
                cnt -= cap[x]
            else:
                last = x
                back.append(x)

print(now)
if len(back):
    print(*back)
else:
    print(-1)
if len(front):
    print(*front)
else:
    print(-1)