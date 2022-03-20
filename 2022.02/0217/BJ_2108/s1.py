import sys
sys.stdin = open('input.txt')

T = int(input())
nums = [0] * T
for i in range(T):
    nums[i] += int(input())

for i in range(T-1, -1, -1):
    for j in range(i):
        if nums[j] > nums[i]:
            nums[j], nums[i] = nums[i], nums[j]

# 평균값
total = 0
for i in nums:
    total += i
avg = total / T
print(round(avg))

# 중앙값
print(nums[round(T/2)])

# 최빈값
def mode(nums):
    if max(nums) < 0:
        cnt = [0] * (abs(min(nums))+1)
    elif min(nums) < 0:
        ngt = abs(min(nums))
        cnt = [0] * (max(nums) + ngt + 1)
    else:
        cnt = [0] * (max(nums)+1)
    for i in nums:
        cnt[i] += 1
    mod_lst = []
    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            if max(nums) < 0:
                mod_lst.append(i-len(cnt))
            elif i > max(nums):
                mod_lst.insert(0, max(nums) - i - 1)
            else:
                mod_lst.append(i)
    if len(mod_lst) == 1:
        return mod_lst[0]
    else:
        return mod_lst[1]
print(mode(nums))

# 범위
print(nums[-1]-nums[0])

