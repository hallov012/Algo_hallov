import sys, copy
sys.stdin = open('input.txt')

def check(x, y):
    possible = [0] * 10
    complete = []
    for num in range(1, 10):
        # rectangle check
        for i in range(3 * (x // 3), 3 * (x // 3 + 1)):
            for j in range(3 * (y // 3), 3 * (y // 3 + 1)):
                if data[i][j] != num:
                    possible[num] += 1
                else:
                    break
        if possible[num] == 1:
            for i in range(9):
                if data[i][y] != num:
                    possible[num] += 1
                else:
                    break
        if possible[num] == 2:
            for j in range(9):
                if data[x][j] != num:
                    possible[num] += 1
                else:
                    break
        if possible[num] == 3:
            complete.append(num)
    return complete

def find(cnt):
    if cnt == m:
        for line in data:
            print(*line)
        exit()
    x, y = blank[cnt]
    possible_num = check(x, y)
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
m = len(blank)
find(0)