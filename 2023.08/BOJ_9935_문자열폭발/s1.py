import sys
sys.stdin = open('input.txt')

word = input()
bomb = input()
stack = []
for char in word:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')