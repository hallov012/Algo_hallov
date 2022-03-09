import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data_a = list(map(int, input().split()))
    data_b = list(map(int, input().split()))
    ans = 0
    min_len, max_len = min(N, M), max(N, M)
    for i in range(max_len - min_len + 1):
        cnt_a = [0] * max_len
        cnt_b = [0] * max_len
        for j in range(min_len):
            if len(data_a) == min_len:
                cnt_a[i+j] = data_a[j]
            else:
                cnt_a = data_a[:]
            if len(data_b) == min_len:
                cnt_b[i+j] = data_b[j]
            else:
                cnt_b = data_b
        sum_multi = 0
        for a in range(max_len):
            sum_multi += cnt_a[a] * cnt_b[a]
        if sum_multi > ans:
            ans = sum_multi
    print(f'#{tc} {ans}')