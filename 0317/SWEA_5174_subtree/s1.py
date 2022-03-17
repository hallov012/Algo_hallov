import sys
sys.stdin = open('input.txt')

def pre_order(node):
    global ans
    if node != 0:
        ans += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E + 2)]
    for i in range(E):
        a, b = temp[2 * i], temp[2 * i + 1]
        if not tree[a][0]:
            tree[a][0] = b
        else:
            tree[a][1] = b

    ans = 0
    pre_order(N)
    print(f'#{tc} {ans}')
