import sys, copy
sys.stdin = open('input.txt')

def rectangle(x, y, num):
    for i in range(3 * (x // 3), 3 * (x // 3 + 1)):
        for j in range(3 * (y // 3), 3 * (y // 3 + 1)):
            if data[i][j] == num:
                return False
    return True

def col(y, num):
    for i in range(9):
        if data[i][y] == num:
            return False
    return True

def row(x, num):
    for j in range(9):
        if data[x][j] == num:
            return False
    return True

def find(cnt):
    if cnt == m:
        for line in data:
            print(*line)
        exit()
    x, y = blank[cnt]
    for num in range(1, 10):
        if rectangle(x, y, num) and col(y, num) and row(x, num):
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
m = len(blank)
find(0)

