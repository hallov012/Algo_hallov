import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][0]
        elif j == len(nums[i])-1:
            nums[i][j] += nums[i-1][j-1]
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
print(max(nums[n-1]))

