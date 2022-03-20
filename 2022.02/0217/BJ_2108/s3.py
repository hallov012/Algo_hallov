import sys
sys.stdin = open('input.txt')

T = int(input())
nums = [0] * T
for i in range(T):
    nums[i] += int(input())

nums.sort()

# 평균값
total = 0
for i in nums:
    total += i
print(round(total/T))

# 중앙값
middle = T // 2
print(nums[middle])

# 최빈값
n = 4000 + 1
cnt = [0] * (2 * n)
for i in nums:
    cnt[i+n] += 1
lst = []
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        lst.append(i)
if len(lst) == 1:
    print(lst[0] - n)
else:
    print(lst[1] - n)

# 범위
print(nums[-1] - nums[0])