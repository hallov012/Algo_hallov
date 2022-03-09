import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sub_set = []
ans = []

def dfs():
    if len(sub_set) == m:
        if sorted(sub_set) not in ans:
            ans.append(sorted(sub_set))
            print(*sub_set)
        return
    for i in range(n):
        if nums[i] not in sub_set:
            sub_set.append(nums[i])
            dfs()
            sub_set.pop()

dfs()