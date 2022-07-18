import sys, math
sys.stdin = open('input.txt')

min_num, max_num = map(int, input().split())
nums = [1] * (max_num - min_num + 1)
num = 2
while num**2 <= max_num:
    # 시간초과를 피하기 위해 min_num보다 큰 배수만 계산하기 위함
    share = min_num // num**2
    while share * (num**2) <= max_num:
        if share * (num**2) - min_num >= 0:
            nums[share*(num**2)-min_num] = 0
        share += 1
    num += 1
print(sum(nums))


