import sys
sys.stdin = open('input.txt')

def pre_order(node):
    if node != 0:
        print(f'{char[node]}', end='')
        pre_order(tree[node][0])
        pre_order(tree[node][1])

def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(f'{char[node]}', end='')
        in_order(tree[node][1])

def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(f'{char[node]}', end='')

n = int(input())
temp = []
char = [''] * (n + 1)
for i in range(1, n + 1):
    data = list(map(str, input().split()))
    char[i] = data[0]
    temp.append(data)

tree = [[0] * 2 for _ in range(n + 1)]
for i in range(n):
    data = temp[i]
    if data[1] != '.':
        tree[i+1][0] = char.index(data[1])
    if data[2] != '.':
        tree[i+1][1] = char.index(data[2])

pre_order(1)
print()
in_order(1)
print()
post_order(1)
print()