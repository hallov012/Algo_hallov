"""
4번 문제와 동일하게 풀이하나 음수가 주어지므로
memorization의 첫 값을 -sys.maxsize로 설정
"""
import sys
from bisect import bisect_left
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
idx = [0] * n
memorization = [-sys.maxsize]

for i in range(n):
    num = nums[i]
    if memorization[-1] < num:
        memorization.append(num)
        idx[i] = len(memorization) - 1
    else:
        idx[i] = bisect_left(memorization, num)
        memorization[idx[i]] = num

ans = len(memorization) - 1
print(ans)
ans_lst = []
for i in range(n-1, -1, -1):
    if idx[i] == ans:
        ans_lst.append(nums[i])
        ans -= 1
print(*reversed(ans_lst))