import sys
sys.stdin = open('input.txt')

word = input()
bomb = input()
stack = []
for char in word:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
ans = ''.join(stack)

if ans == '':
    print('FRULA')
else:
    print(ans)