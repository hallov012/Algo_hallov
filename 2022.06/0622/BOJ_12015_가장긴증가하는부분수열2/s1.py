"""
이분탐색을 이용한 LIS(Longest increasing Subsequence: 최장 증가 부분 수열)
주어진 배열의 인덱스를 하나씩 살펴보며, 그 숫자가 들어갈 위치를 이분탐색으로 탐색
시간복잡도 => O(nlog n)
"""

import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
memorization = [0]
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
print(len(memorization)-1)