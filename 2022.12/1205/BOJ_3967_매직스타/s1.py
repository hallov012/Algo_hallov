import sys
sys.stdin = open('input.txt')

def sol(stars):
    idx = 0
    for i in range(x):
        for j in range(y):
            if arr[i][j] != '.':
                if arr[i][j] == 'x':
                    arr[i][j] = chr(stars[idx]+64)
                idx += 1
    for i in range(x):
        print(("").join(arr[i]))

def check(data):
    for case in cases:
        cnt = 0
        for i in range(4):
            cnt += data[case[i]]
        if cnt != 26:
            return False
    return True

def dfs(cnt):
    if cnt == blank:
        if check(stars):
            sol(stars)
            exit()
    for i in range(12):
        if not stars[i]:
            for j in range(1, 13):
                if not visited[j]:
                    stars[i] = j
                    visited[j] = 1
                    dfs(cnt+1)
                    stars[i] = 0
                    visited[j] = 0

input = sys.stdin.readline

x, y = 5, 9
arr = [list(input().rstrip()) for _ in range(x)]
stars = [0] * 12
visited = [0] * 13
idx = 0
for i in range(x):
    for j in range(y):
        if arr[i][j] != '.':
            if arr[i][j] == 'x':
                idx += 1
            else:
                stars[idx] = ord(arr[i][j]) - 64
                visited[ord(arr[i][j]) - 64] = 1
                idx += 1
blank = stars.count(0)
cases = [[0, 2, 5, 7], [0, 3, 6, 10], [1, 2, 3, 4], [7, 8, 9, 10], [1, 5, 8, 11], [4, 6, 9, 11]]
dfs(0)