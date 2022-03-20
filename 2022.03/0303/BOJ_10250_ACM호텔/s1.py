import sys
sys.stdin = open('input.txt')

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    arr = [[0] * w for _ in range(h)]
    a = 1
    i, j = 0, 0
    while a < n:
        arr[i][j] = a
        i += 1
        a += 1
        if i == h:
            i = 0
            j += 1
    ans = 100 * (i + 1) + (j + 1)
    print(ans)
