import sys
sys.stdin = open('input.txt')

def dfs(row1, row2, idx):
    a, b = idx, nums[idx]
    row1.add(a)
    row2.add(b)
    if b in row1:
        if row1 == row2:
            ans.update(row1)
        return
    dfs(row1, row2, b)

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
ans = set()

for i in range(1, n+1):
    if i not in ans:
        dfs(set(), set(), i)

ans = sorted(list(ans))
print(len(ans))
for num in ans:
    print(num)