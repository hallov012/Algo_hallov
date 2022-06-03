import sys
sys.stdin = open('input.txt')

word = input()
ans = 0
stack = []
for char in word:
    if char == '(':
        stack.append('(')
    elif char == ')':
        if not stack:
            ans += 1
        else:
            stack.pop()
if stack:
    ans += len(stack)
print(ans)