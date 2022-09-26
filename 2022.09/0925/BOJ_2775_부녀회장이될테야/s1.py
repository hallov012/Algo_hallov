import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    cnt = [[0] * (n+1) for _ in range(k+1)]
    cnt[0] = list(range(n+1))
    for i in range(1, k+1):
        for j in range(1, n+1):
            cnt[i][j] = sum(cnt[i-1][:j+1])
    print(cnt[k][n])