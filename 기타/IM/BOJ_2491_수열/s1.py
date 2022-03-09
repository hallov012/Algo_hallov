import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
cnt_lst = []
i = 1
cnt = 1
while 1:
    if i == n:
        cnt_lst.append(cnt)
        break
    if nums[i-1] >= nums[i]:
        cnt += 1
    elif nums[i-1] < nums[i]:
        cnt_lst.append(cnt)
        cnt = 1
    i += 1

i = 1
cnt = 1
while 1:
    if i == n:
        cnt_lst.append(cnt)
        break
    if nums[i-1] <= nums[i]:
        cnt += 1
    elif nums[i-1] > nums[i]:
        cnt_lst.append(cnt)
        cnt = 1
    i += 1
print(max(cnt_lst))
