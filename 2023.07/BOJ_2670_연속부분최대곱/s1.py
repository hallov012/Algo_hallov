import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [float(input()) for _ in range(n)]
for i in range(1, n):
    nums[i] = max(nums[i], nums[i] * nums[i-1])
ans = max(nums)
print('%0.3f' % ans)
