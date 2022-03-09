import sys
sys.stdin = open('input.txt')

n = 4

for _ in range(4):
    data = list(map(int, input().split()))
    box_1 = [data[0:2], data[2:4]]
    box_2 = [data[4:6], data[6:9]]

    if box_1[1][0] < box_2[0][0] or box_1[0][0] > box_2[1][0] or box_1[1][1] < box_2[0][1] or box_1[0][1] > box_2[1][1]:
            print('d')

    elif box_1[1][0] == box_2[0][0] or box_1[0][0] == box_2[1][0]:
        if box_1[1][1] == box_2[0][1] or box_1[0][1] == box_2[1][1]:
            print('c')
        else:
            print('b')
    elif box_1[1][1] == box_2[0][1] or box_1[0][1] == box_2[1][1]:
        print('b')
    else:
        print('a')