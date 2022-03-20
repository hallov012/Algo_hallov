import sys
sys.stdin = open('input.txt')

n = int(input())
xy_dic = {}
for i in range(n):
    x, y = map(int, input().split())
    if x not in xy_dic:
        xy_dic[x] = [y]
    else:
        xy_dic[x] += [y]
sort_x_dic = sorted(xy_dic.items())
for i in sort_x_dic:
    sort_y = sorted(i[1])
    for j in sort_y:
        print(i[0], j)





