import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    start_idx = []
    for i in range(102):
        if data[0][i]:
            start_idx.append(i)
    cnt_lst = []
    for c in start_idx:
        cnt = 0
        r = 0
        while r < 100:
            if data[r][c-1]:
                while data[r][c-1]:
                    c -= 1
                    cnt += 1
            elif data[r][c+1]:
                while data[r][c+1]:
                    c += 1
                    cnt += 1
            r += 1
            cnt += 1
        cnt_lst.append(cnt)
    min_cnt = min(cnt_lst)
    ans_idx = []
    for i in range(len(cnt_lst)):
        if cnt_lst[i] == min_cnt:
            ans_idx.append(i)
    print(f'#{tc} {start_idx[ans_idx[-1]]-1}')
