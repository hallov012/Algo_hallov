import sys
import heapq

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    k = int(input())
    end = [0] * k  # 삭제한 idx 표시해줄 item
    min_h, max_h = [], []
    for i in range(k):
        command, a = input().split()
        if command == 'I':
            heapq.heappush(min_h, (int(a), i))
            heapq.heappush(max_h, (-1 * int(a), i))
        elif command == 'D':
            if a == '-1':       # 최솟값 삭제
                while min_h:
                    if end[min_h[0][1]] == 1:
                        heapq.heappop(min_h)
                    else:
                        break
                if min_h:
                    min = min_h[0][1]
                    end[min] = 1
                    heapq.heappop(min_h)
            elif a == '1':    # 최댓값 삭제
                while max_h:
                    if end[max_h[0][1]] == 1:
                        heapq.heappop(max_h)
                    else:
                        break
                if max_h:
                    max = max_h[0][1]
                    end[max] = 1
                    heapq.heappop(max_h)
    while min_h:
        if end[min_h[0][1]] == 1:
            heapq.heappop(min_h)
        else:
            break
    while max_h:
        if end[max_h[0][1]] == 1:
            heapq.heappop(max_h)
        else:
            break
    if min_h:
        print(-1 * max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')

