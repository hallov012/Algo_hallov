import sys
sys.stdin = open('input.txt')

S = input()
stack = []
left = ''
ans = 0
for char in S:
    if char == '(':
        stack.append([ans-1, left])
        ans = 0
    elif char == ')':
        cnt, num = stack.pop()
        ans = ans * num + cnt
    else:
        ans += 1
        left = int(char)
print(ans)