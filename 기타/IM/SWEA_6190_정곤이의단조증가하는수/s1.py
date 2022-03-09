import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_multi = 0
    for i in range(n-1):
        for j in range(i+1, n):
            check_num = nums[i] * nums[j]
            check_copy = check_num
            q = deque([])
            while check_num > 0:
                q.appendleft(check_num % 10)
                check_num = check_num // 10
            a = 0
            while 1:
                if a == len(q)-1:
                    if check_copy > max_multi:
                        max_multi = check_copy
                        break
                elif q[a] > q[a+1]:
                    break
                else:
                    pass
                a += 1
    print(f'#{tc} {max_multi}')





