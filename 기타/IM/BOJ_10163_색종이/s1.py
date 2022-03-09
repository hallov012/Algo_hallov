import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    r, c, w, h = map(int, input().split())
    for i in range(r, r + w):
        for j in range(c, c + h):
            arr[i][j] = n
cnt = [0] * (N+1)
for n in range(1, N+1):
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == n:
                cnt[n] += 1
    print(cnt[n])
