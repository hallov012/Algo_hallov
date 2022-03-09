import sys
sys.stdin = open('input.txt')

def check_bingo(lst):
    cnt = 0
    for i in range(len(lst)):
        if not sum(lst[i]):
            cnt += 1
    for j in range(len(lst)):
        col_lst = []
        for i in range(len(lst)):
            col_lst.append(lst[i][j])
        if not sum(col_lst):
            cnt += 1
    cross_lst = []
    for i in range(len(lst)):
        cross_lst.append(lst[i][i])
    if not sum(cross_lst):
        cnt += 1
    cross_lst_2 = []
    for i in range(len(lst)):
        cross_lst_2.append(lst[i][len(lst)-i-1])
    if not sum(cross_lst_2):
        cnt += 1
    return cnt

bingo = [list(map(int, input().split())) for _ in range(5)]
location = [[] for _ in range(26)]
for i in range(5):
    for j in range(5):
        num = bingo[i][j]
        location[num] = [i, j]
nums = []
for i in range(5):
    nums += map(int, input().split())
for i in range(len(nums)):
    a, b = location[nums[i]][0], location[nums[i]][1]
    bingo[a][b] = 0
    check = check_bingo(bingo)
    if check >= 3:
        print(i+1)
        break
