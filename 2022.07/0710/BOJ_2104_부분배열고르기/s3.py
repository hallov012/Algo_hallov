"""
분할 정복을 써라...
https://www.acmicpc.net/problem/6549
6549번과 비슷한 과정 => 참고
"""

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def find(left, right):
    global ans
    if left == right:
        ans = max(ans, nums[left] ** 2)
        return
    mid = (left+right)//2
    min_num = min(nums[mid], nums[mid+1])
    cnt = nums[mid] + nums[mid+1]
    ans = max(ans, min_num * cnt)
    i, j = 0, 0
    for _ in range(right-left-1):
        if mid-i == left:
            j += 1
            cnt += nums[mid + j + 1]
        elif mid+j+1 == right:
            i += 1
            cnt += nums[mid - i]
        else:
            if nums[mid-i-1] >= nums[mid+j+2]:
                i += 1
                cnt += nums[mid-i]
            else:
                j += 1
                cnt += nums[mid+j+1]
        min_num = min(min_num, nums[mid-i], nums[mid+j+1])
        ans = max(ans, min_num * cnt)
    find(left, mid)
    find(mid+1, right)

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = 0
find(0, n-1)
print(ans)