import sys
sys.stdin = open('input.txt')

S = input().rstrip()

ans = 0
stack = []
left = 0
for s in S:
    if s == '(':
        stack.append([left, ans-1])
        ans = 0
    elif s == ')':
        num, cnt = stack.pop()
        ans = ans * num + cnt
    else:
        ans += 1
        left = int(s)

print(ans)