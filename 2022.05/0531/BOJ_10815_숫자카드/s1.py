import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
questions = list(map(int, input().split()))
ans = []
nums.sort()
for num in questions:
    left, right = 0, n-1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            flag = True
            ans.append(1)
            break
        elif nums[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    if not flag:
        ans.append(0)
print(*ans)