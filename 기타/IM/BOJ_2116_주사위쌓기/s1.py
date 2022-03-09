import sys
import copy
sys.stdin = open('input.txt')

def counter(int):
    if int == 0:
        return 5
    if int == 5:
        return 0
    if int == 1:
        return 3
    if int == 3:
        return 1
    if int == 2:
        return 4
    if int == 4:
        return 2



t = int(input())
data = [list(map(int, input().split())) for _ in range(t)]
sum_lst = []
for j in range(6):          # 맨 아래에 dice를 놓는 6가지 경우가 있다!
    data_1 = copy.deepcopy(data)
    bottom , top = data[0][j], data[0][counter(j)]
    data_1[0].remove(bottom)
    data_1[0].remove(top)
    sum = max(data_1[0])
    for i in range(1,t):
        bottom = top
        top = data[i][counter(data[i].index(bottom))]
        data_1[i].remove(bottom)
        data_1[i].remove(top)
        sum += max(data_1[i])
    sum_lst.append(sum)
print(max(sum_lst))