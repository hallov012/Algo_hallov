"""
단일 idx를 min값으로 가지는 최대 구간 합 구하기 => 실패
"""
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in range(n):
    cnt = nums[i]
    a = i-1
    while a >= 0 and nums[a] >= nums[i]:
        cnt += nums[a]
        a -= 1
    b = i+1
    while b < n and nums[b] > nums[i]:
        cnt += nums[b]
        b += 1
    ans = max(ans, nums[i]*cnt)
print(ans)