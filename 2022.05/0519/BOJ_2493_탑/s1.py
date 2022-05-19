import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
ans = []
stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > nums[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, nums[i]])

print(*ans)