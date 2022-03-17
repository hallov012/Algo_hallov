import sys
sys.stdin = open('input.txt')

def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        if tree[node][2] in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if tree[node][2] == '+':
                stack.append(a + b)
            elif tree[node][2] == '-':
                stack.append(a - b)
            elif tree[node][2] == '*':
                stack.append(a * b)
            elif tree[node][2] == '/':
                stack.append(a / b)
        else:
            stack.append(int(tree[node][2]))


for tc in range(1, 11):
    n = int(input())
    tree = [[0] * 3 for _ in range(n + 1)]
    for i in range(1, n+1):
        data = input().split()
        tree[i][2] = data[1]
        if len(data) > 2:
            tree[i][0] = int(data[2])
            if len(data) > 3:
                tree[i][1] = int(data[3])
    stack = []
    post_order(1)
    print(f'#{tc} {int(stack[0])}')



