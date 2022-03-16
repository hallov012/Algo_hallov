import sys
sys.stdin = open('input.txt')

def post_order(node):
    global ans_word
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        ans_word.append(check[node])


for tc in range(1, 11):
    n = int(input())
    tree = [[0] * 2 for _ in range(n + 1)]
    check = [''] * (n + 1)
    ans_word = []
    for i in range(1, n+1):
        data = input().split()
        if len(data) == 2:
            check[int(data[0])] = data[1]
        elif len(data) == 3:
            check[int(data[0])] = data[1]
            tree[int(data[0])][0] = int(data[2])
        else:
            check[int(data[0])] = data[1]
            tree[int(data[0])][0] = int(data[2])
            tree[int(data[0])][1] = int(data[3])
    post_order(1)
    stack = []
    for char in ans_word:
        if char in '+-*/':
            b = int(stack.pop())
            a = int(stack.pop())
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            else:
                stack.append(a / b)
        else:
            stack.append(char)
    ans = int(stack[0])
    print(f'#{tc} {ans}')

