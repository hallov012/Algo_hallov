import sys
sys.stdin = open('input.txt')

def find_sum(idx, end, sum, num_lst, result):
    if idx >= end:
        result.append(sum)
        return
    find_sum(idx+1, end, sum+num_lst[idx], num_lst, result)
    find_sum(idx+1, end, sum, num_lst, result)

def binary_search(start, end, key):
    while start < end:
        mid = (start + end) // 2
        if right_sum[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return end

input = sys.stdin.readline

n, c = map(int, input().split())
nums = list(map(int, input().split()))
left_lst = nums[:n//2]
right_lst = nums[n//2:]
left_sum, right_sum = [], []

find_sum(0, len(left_lst), 0, left_lst, left_sum)
find_sum(0, len(right_lst), 0, right_lst, right_sum)

right_sum.sort()
ans = 0
for num in left_sum:
    if c - num < 0:
        continue
    ans += binary_search(0, len(right_sum), c-num)

print(ans)


