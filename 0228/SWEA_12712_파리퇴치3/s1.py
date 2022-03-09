import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            cnt_1, cnt_2 = arr[i][j], arr[i][j]
            a = 1
            while a < m:
                if 0 <= i - a:
                    cnt_1 += arr[i-a][j]
                if i + a < n:
                    cnt_1 += arr[i+a][j]
                if 0 <= j - a:
                    cnt_1 += arr[i][j-a]
                if j + a < n:
                    cnt_1 += arr[i][j+a]
                if 0 <= i - a and 0 <= j - a:
                    cnt_2 += arr[i-a][j-a]
                if i + a < n and j + a < n:
                    cnt_2 += arr[i+a][j+a]
                if i + a < n and 0 <= j - a:
                    cnt_2 += arr[i+a][j-a]
                if 0 <= i - a and j + a < n:
                    cnt_2 += arr[i-a][j+a]
                a += 1
            if ans <= cnt_1:
                ans = cnt_1
            if ans <= cnt_2:
                ans = cnt_2
    print(f'#{tc} {ans}')
