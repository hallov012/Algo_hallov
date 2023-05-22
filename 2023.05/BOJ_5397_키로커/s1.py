import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str = input().rstrip()
    stack = []
    cursor = -1
    for char in str:
        if char == '<':
            if cursor > 0:
                cursor -= 1
        elif char == '>':
            if cursor < len(stack)-1:
                cursor += 1
        elif char == '-':
            if stack and cursor != -1:
                stack.pop(cursor)
                cursor -= 1
        else:
            cursor += 1
            stack.insert(cursor, char)

    print(''.join(stack))

