import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    cnt = [0] * 101
    for i in data:
        cnt[i] += 1
    max_box = max(data)
    min_box = min(data)
    i = 0
    while i < n:
        cnt[max_box] -= 1
        cnt[max_box - 1] += 1
        cnt[min_box] -= 1
        cnt[min_box + 1] += 1
        while cnt[max_box] == 0:
            max_box -= 1
        while cnt[min_box] == 0:
            min_box += 1
        if max_box - min_box <= 1:
            break
        i += 1
    print(f'#{tc} {max_box - min_box}')