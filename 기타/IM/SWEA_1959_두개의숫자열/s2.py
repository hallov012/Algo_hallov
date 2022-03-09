import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data_a = list(map(int, input().split()))
    data_b = list(map(int, input().split()))
    min_len, max_len = min(N, M), max(N, M)
    ans = 0
    if N == max_len:
        long_lst, short_lst = data_a, data_b
    else:
        long_lst, short_lst = data_b, data_a
    for i in range(max_len - min_len + 1):
        multi_sum = 0
        for j in range(min_len):
            multi_sum += short_lst[j] * long_lst[i+j]
        if multi_sum > ans:
            ans = multi_sum
    print(f'#{tc} {ans}')
