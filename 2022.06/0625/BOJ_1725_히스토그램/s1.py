import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
stack = []
ans = 0
for i in range(n):
    while stack and data[stack[-1]] > data[i]:
        h = data[stack[-1]]
        stack.pop()
        if stack:
            w = i - stack[-1] - 1
        else:
            w = i
        ans = max(ans, h * w)
    stack.append(i)

while stack:
    h = data[stack[-1]]
    stack.pop()
    if stack:
        w = n - stack[-1] - 1
    else:
        w = n
    ans = max(ans, h * w)

print(ans)


