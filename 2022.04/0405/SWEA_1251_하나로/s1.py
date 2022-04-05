import sys
sys.stdin = open('input.txt')

def prim():
    for _ in range(n-1):
        min_idx = -1
        min_value = inf
        for i in range(n):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1
        for j in range(n):
            if not visited[j] and g[min_idx][j] < key[j]:
                key[j] = g[min_idx][j]
    return sum(key)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    e = float(input())
    inf = 1000000 ** 2
    g = [[inf] * n for _ in range(n)]
    visited = [0] * n
    key = [inf] * n
    key[0] = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                w = (x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2
                g[i][j] = w
                g[j][i] = w
    ans = prim()
    print(f'#{tc} {round(ans * e)}')
