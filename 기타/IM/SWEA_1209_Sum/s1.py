import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    for i in range(100):
        if sum(data[i]) > ans:
            ans = sum(data[i])
    for i in range(100):
        col_lst = list(zip(*data))[i]
        if sum(col_lst) > ans:
            ans = sum(col_lst)
    cross_lst = []
    cross_lst2 = []
    for i in range(100):
        cross_lst.append(data[i][i])
        cross_lst2.append(data[i][100-i-1])
        if sum(cross_lst) > ans:
            ans = sum(cross_lst)
        if sum(cross_lst2) > ans:
            ans = sum(cross_lst2)
    print(f'#{tc} {ans}')