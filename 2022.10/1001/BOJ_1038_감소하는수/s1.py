import sys
from itertools import combinations
sys.stdin = open('input.txt')

n = int(input())
nums = []
for i in range(1, 11):
    cases = list(combinations(range(10), i))
    for case in cases:
        case = list(case)
        case.sort(reverse=True)
        nums.append(int("".join(map(str, case))))

nums.sort()
if n >= len(nums):
    print(-1)
else:
    print(nums[n])
