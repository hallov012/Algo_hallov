word = input()

isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
stack = []
result = ''
for char in word:
    if char in '+-*/()':
        if stack:
            if char == ')':
                while stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
            else:
                while stack and isp[char] <= icp[stack[-1]]:
                    result += stack.pop()
                stack.append(char)
        else:
            stack.append(char)
    else:
        result += char
while stack:
    result += stack.pop()
print(result)