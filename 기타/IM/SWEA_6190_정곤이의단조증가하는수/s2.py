import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    max_multi = -1
    for i in range(n-1):
        for j in range(i+1, n):
            check_num = nums[i] * nums[j]
            check_copy = check_num
            lst = []
            while check_num > 0:
                lst.append(check_num % 10)
                check_num = check_num // 10
            a = len(lst)-1
            while 1:
                if a == 0:
                    max_multi = max(max_multi, check_copy)
                    break
                elif lst[a] > lst[a-1]:
                    break
                a -= 1
    print(f'#{tc} {max_multi}')