import sys
sys.stdin = open('input.txt')

def num_check(x, y):
    possible = [0] * 10
    for i in range(3 * (x//3), 3 * (x//3 + 1)):
        for j in range(3 * (y//3), 3 * (y//3 + 1)):
            possible[data[i][j]] += 1
    for i in range(9):
        possible[data[i][y]] += 1
    for j in range(9):
        possible[data[x][j]] += 1
    possible_num = []
    for i in range(1, 10):
        if not possible[i]:
            possible_num.append(i)
    return possible_num

def find(cnt):
    if cnt == m:
        for line in data:
            print(*line)
        exit()
    x, y = blank[cnt]
    possible_num = num_check(x, y)
    for num in possible_num:
        data[x][y] = num
        find(cnt+1)
        data[x][y] = 0

input = sys.stdin.readline

data = []
blank = []
for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        if not line[j]:
            blank.append((i, j))
    data.append(line)
# print(data, blank)
m = len(blank)
find(0)


