import sys
sys.stdin = open('input.txt')

T = int(input())
nums = [0] * T
for i in range(T):
    nums[i] += int(input())

def sort(nums):
    for i in range(T - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums
sort(nums)

def mean(nums):
    total = 0
    for num in nums:
        total += num
    return round(total/len(nums))
print(mean(nums))
print(nums[(T-1)//2])

def mode(nums):
    mode_lst = []
    if nums[-1] < 0:
        cnt = [0] * (-nums[0] + 1)
        for i in nums:
            cnt[i] += 1
        for i in range(len(cnt)):
            if cnt[i] == max(cnt):
                mode_lst.append(i - len(cnt))
    elif nums[0] < 0:
        cnt = [0] * (nums[-1] - nums[0] + 1)
        for i in nums:
            cnt[i] += 1
        for i in range(len(cnt)):
            if cnt[i] == max(cnt):
                if i > nums[-1]:
                    mode_lst.insert(0, nums[-1]-i-1)
                else:
                    mode_lst.append(i)
    else:
        cnt = [0] * (nums[-1] + 1)
        for i in nums:
            cnt[i] += 1
        for i in range(len(cnt)):
            if cnt[i] == max(cnt):
                mode_lst.append(i)
    if len(mode_lst) > 1:
        return mode_lst[1]
    else:
        return mode_lst[0]

print(mode(nums))
print(nums[-1]-nums[0])