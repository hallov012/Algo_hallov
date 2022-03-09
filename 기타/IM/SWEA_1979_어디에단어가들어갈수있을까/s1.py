import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    arr = [[0] * (n+2) for _ in range(n+2)]
    ans = 0
    for i in range(n):
        for j in range(n):
            arr[i+1][j+1] = data[i][j]
    for i in range(n+2):
        for j in range(n+1):
            if not arr[i][j]:
                c = 1
                cnt = 0
                while 1:
                    if arr[i][j+c] and j + c < n + 2:
                        cnt += 1
                        c += 1
                    else:
                        break
                if cnt == k:
                    ans += 1
    for j in range(n+2):
        for i in range(n+1):
            if not arr[i][j]:
                c = 1
                cnt = 0
                while 1:
                    if arr[i+c][j] and i + c < n + 2:
                        cnt += 1
                        c += 1
                    else:
                        break
                if cnt == k:
                    ans += 1
    print(f'#{tc} {ans}')



