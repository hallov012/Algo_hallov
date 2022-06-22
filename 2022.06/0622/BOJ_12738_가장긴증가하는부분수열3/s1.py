"""
2번 문제와 다른점 => 음수 추가
memorization의 0번째 인덱스에 0이 아닌 -sys.maxsize로 추가
"""

import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
memorization = [-sys.maxsize]
for num in nums:
    if memorization[-1] < num:
        memorization.append(num)
    else:
        left = 0
        right = len(memorization)
        while left < right:
            mid = (left + right) // 2
            if memorization[mid] < num:
                left = mid + 1
            else:
                right = mid
        memorization[right] = num
    print(memorization)
print(len(memorization)-1)