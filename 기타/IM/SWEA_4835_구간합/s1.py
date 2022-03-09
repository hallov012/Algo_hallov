import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    max_cnt = 0
    min_cnt = 10000 * m
    for i in range(n-m+1):
        cnt = 0
        for j in range(m):
            cnt += data[i+j]
        max_cnt = max(max_cnt, cnt)
        min_cnt = min(min_cnt, cnt)
    ans = max_cnt - min_cnt
    print(f'#{tc} {ans}')



