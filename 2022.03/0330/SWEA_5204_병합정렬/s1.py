import sys
sys.stdin = open('input.txt')

def merge(left, right):
    global cnt
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    sorted_list = []
    l = r = 0

    while len(sorted_list) != len(left) + len(right):
        if left[l] <= right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
        if r == len(right):
            sorted_list += left[l:]
            cnt += 1
            break
        if l == len(left):
            sorted_list += right[r:]
            break
    return sorted_list


def partition(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = partition(nums[:mid])
    right = partition(nums[mid:])
    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    sort_nums = partition(nums)
    print(f'#{tc}', sort_nums[n//2], cnt)
