import sys
sys.stdin = open('input.txt')

n = int(input())
h_lst = list(map(int, input().split()))
ans = [0] * n
stack = []
for i in range(n):
    h = h_lst[i]
    while stack and stack[-1][0] <= h:
        stack.pop()
    if stack:
        ans[i] = stack[-1][1]
    stack.append((h, i + 1))

print(*ans)