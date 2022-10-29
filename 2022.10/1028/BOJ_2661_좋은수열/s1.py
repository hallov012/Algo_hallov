import sys
sys.stdin = open('input.txt')

def find(idx):
    for i in range(1, (idx//2) + 1):
        if nums[-i:] == nums[-2*i:-i]:
            return -1
    if idx == n:
        for i in range(n):
            print(nums[i], end="")
        return 0
    for i in range(1, 4):
        nums.append(i)
        if find(idx+1) == 0:
            return 0
        nums.pop()

n = int(input())
nums = []
find(0)

