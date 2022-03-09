import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
    ans = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans += 1
    print(f'#{tc} {ans}')

