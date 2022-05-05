import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

k = int(input())
stack = []
for i in range(k):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))