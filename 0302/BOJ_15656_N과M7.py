import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sub_set = []

def dfs():
    if len(sub_set) == m:
        print(*sub_set)
        return
    for i in range(n):
        sub_set.append(nums[i])
        dfs()
        sub_set.pop()

dfs()