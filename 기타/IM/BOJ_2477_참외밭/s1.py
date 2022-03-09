import sys
sys.stdin = open('input.txt')

k = int(input())
data = [list(map(int, input().split())) for _ in range(6)]
# 1: 오른쪽, 2: 왼쪽, 3: 아래, 4:
h_list = []
w_list = []
for i in range(6):
    if data[i][0] == 3 or data[i][0] == 4:
        h_list.append(data[i][1])
    if data[i][0] == 1 or data[i][0] == 2:
        w_list.append(data[i][1])
h = max(h_list)
w = max(w_list)
empty = 0
for i in range(6):
    if data[i][0] == data[(i+2) % 6][0]:
        if data[(i+1) % 6][0] == data[(i+3) % 6][0]:
            empty = data[(i+1) % 6][1] * data[(i+2) % 6][1]
        else:
            empty = data[i][1] * data[(i+1) % 6][1]
        if empty != 0:
            break
area = h * w - empty
print(area * k)