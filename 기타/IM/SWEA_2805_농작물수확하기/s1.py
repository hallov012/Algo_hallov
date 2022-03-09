import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input())) for _ in range(n)]
    idx = n // 2
    idx_copy = idx
    ans = 0
    i = 0
    while idx >= 0:
        if not idx:
            for j in range(n):
                ans += data[i][j]
        else:
            for j in range(idx, n-idx):
                ans += data[i][j]
                ans += data[n-i-1][j]
        i += 1
        idx -= 1
    print(f'#{tc} {ans}')



