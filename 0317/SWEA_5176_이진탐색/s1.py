import sys
sys.stdin = open('input.txt')

def in_order(node):
    global cnt
    if node != 0:
        in_order(tree[node][0])
        order[node] = cnt
        cnt += 1
        in_order(tree[node][1])

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tree = [[0] * 2 for _ in range(n + 1)]
    que = [1]
    while que:
        i = que.pop(0)
        if 2 * i < n + 1:
            tree[i][0] = 2 * i
            que.append(2 * i)
        if 2 * i + 1 < n + 1:
            tree[i][1] = 2 * i + 1
            que.append(2 * i + 1)
    order = [0] * (n + 1)
    cnt = 1
    in_order(1)
    print(f'#{tc}', order[1], order[n//2])