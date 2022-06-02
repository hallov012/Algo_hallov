import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def find_sum(nums, sum_lst):
    for i in range(len(nums)):
        sum = nums[i]
        sum_lst[sum] += 1
        for j in range(i+1, len(nums)):
            sum += nums[j]
            sum_lst[sum] += 1

input = sys.stdin.readline

t = int(input())
n = int(input())
a_nums = list(map(int, input().split()))
m = int(input())
b_nums = list(map(int, input().split()))
a_sum = defaultdict(int)
b_sum = defaultdict(int)
ans = 0

find_sum(a_nums, a_sum)
find_sum(b_nums, b_sum)

a_key = list(a_sum.keys())
b_key = list(b_sum.keys())
a_key.sort()
b_key.sort()

left = 0
right = len(b_key) - 1
while left < len(a_sum) and right >= 0:
    temp = a_key[left] + b_key[right]
    if temp == t:
        ans += a_sum[a_key[left]] * b_sum[b_key[right]]
        left += 1
        right -= 1
    elif temp > t:
        right -= 1
    else:
        left += 1

print(ans)