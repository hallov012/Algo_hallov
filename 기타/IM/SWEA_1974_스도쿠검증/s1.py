import sys
sys.stdin = open('input.txt')

def check(lst):
    cnt = [0] * 9
    for num in lst:
        cnt[num-1] += 1
    check_cnt = list(set(cnt))
    if len(check_cnt) == 1 and check_cnt[0]:
        return 0
    else:
        return 1

T = int(input())

for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    for i in range(9):
        result += check(data[i])

    for j in range(9):
        col_lst = []
        for i in range(9):
            col_lst.append(data[i][j])
        result += check(col_lst)

    for i in range(3):
        for j in range(3):
            box_lst = []
            for a in range(3):
                for b in range(3):
                    box_lst.append(data[3*i+a][3*j+b])
            result += check(box_lst)

    if not result:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')




