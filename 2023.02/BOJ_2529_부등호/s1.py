import sys
from itertools import permutations
sys.stdin = open('input.txt')

def check(a, b, idx):
    if orders[idx] == '<':
        return a < b
    else:
        return a > b
    return False

def dfs(cnt, )

n = int(input())
orders = list(map(str, input().split()))
nums = list(range(10))
cases = list(permutations(nums, n+1))
ans = []
for case in cases:
    for i in range(n):
        if not check(case[i], case[i+1], i):
            break
    else:
        ans.append(case)
ans.sort()
print(('').join(list(map(str, ans[-1]))))
print(('').join(list(map(str, ans[0]))))
