import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
idx = {}
for i in range(n):
    idx[nums[i]] = i

ans = 0
nums.sort()
for i in range(n):
    num = nums[i]
    if i == idx[num]:
        ans += num
    else:
        ans += num + i - idx[num]
print(ans)

