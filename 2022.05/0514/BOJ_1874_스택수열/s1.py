import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
stack = []
cnt = 1
flag = True
ans = ''
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans += '+'
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans += '-'
    else:
        flag = False
if not flag:
    print('NO')
else:
    for char in ans:
        print(char)