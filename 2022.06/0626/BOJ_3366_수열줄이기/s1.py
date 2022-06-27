import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
ans = 0
stack = [data[0]]
for i in range(1, n):
    if stack[0] > data[i]:
        while stack and stack[-1] <= data[i]:
            stack.pop()
            ans += min(stack[-1], data[i])
    else:
        ans += sum(stack[:-1]) + data[i]
        stack = []
    stack.append(data[i])

print(ans + sum(stack[:-1]))

