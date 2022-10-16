import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def r_calulation():
    new = []
    max_len = 0
    for i in range(len(arr)):
        line = []
        cnt = defaultdict(int)
        for num in arr[i]:
            if num:
                cnt[num] += 1
        cnt_sort = sorted(cnt.items(), key=lambda x:(x[1], x[0]))
        for a, b in cnt_sort:
            line.append(a)
            line.append(b)
        if len(line) > 100:
            line = line[:100]
        new.append(line)
        max_len = max(max_len, len(line))
    for i in range(len(new)):
        while len(new[i]) < max_len:
                new[i].append(0)
    return new

def c_calculation():
    data = []
    max_len = 0
    for j in range(len(arr[0])):
        column = []
        for i in range(len(arr)):
            column.append(arr[i][j])
        line = []
        cnt = defaultdict(int)
        for num in column:
            if num:
                cnt[num] += 1
        cnt_sort = sorted(cnt.items(), key=lambda x:(x[1], x[0]))
        for a, b in cnt_sort:
            line.append(a)
            line.append(b)
        if len(line) > 100:
            line = line[:100]
        data.append(line)
        max_len = max(max_len, len(line))
    for i in range(len(data)):
        while len(data[i]) < max_len:
            data[i].append(0)
    new = [[0] * len(data) for _ in range(len(data[0]))]
    for j in range(len(data[0])):
        for i in range(len(data)):
            new[j][i] = data[i][j]
    return new

input = sys.stdin.readline

r, c, k = map(int, input().split())
r, c = r-1, c-1
arr = [list(map(int, input().split())) for _ in range(3)]
ans = 0
while ans <= 100:
    if r < len(arr) and c < len(arr[0]):
        if arr[r][c] == k:
            print(ans)
            break
    if len(arr) >= len(arr[0]):
        arr = r_calulation()
    else:
        arr = c_calculation()
    ans += 1
if ans == 101:
    print(-1)