import sys
sys.stdin = open('input.txt')

n = int(input())
nums = list(map(int, input().split()))
ans = [0] * n
stack = []
for i in range(n):
    if not stack:
        stack.append(i)
    else:
        if nums[stack[-1]] < nums[i]:
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        else:
            stack.append(i)

for i in range(n):
    if i == n-1:
        print(-1)
    else:
        if not ans[i]:
            print(-1, end=' ')
        else:
            print(ans[i], end=' ')
