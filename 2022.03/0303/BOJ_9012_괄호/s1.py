import sys
sys.stdin = open('input.txt')

n = int(input())

for tc in range(n):
    word = input()
    stack = []
    ans = 1
    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                ans = 0
                break
    if stack:
        ans = 0

    if ans:
        print('YES')
    else:
        print('NO')
