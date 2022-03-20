import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, l = map(int, input().split())
    node = [0] * (n + 1)
    for _ in range(m):
        idx, num = map(int, input().split())
        node[idx] = num
    if n % 2:
        for i in range(n - 1, 0, -2):
            node[i // 2] = node[i] + node[i + 1]
    else:     
        node[n // 2] = node[n]
        for i in range(n - 2, 0, -2):
            node[i // 2] = node[i] + node[i + 1]
    print(f'#{tc} {node[l]}')