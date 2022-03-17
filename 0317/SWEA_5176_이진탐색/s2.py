import sys
sys.stdin = open('input.txt')

def sol(node):
    global num
    if node < n + 1:
        sol(node * 2)
        tree[node] = num
        num += 1
        sol(node * 2 + 1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n + 1)
    num = 1
    sol(1)
    print(f'#{tc}', tree[1], tree[n//2])