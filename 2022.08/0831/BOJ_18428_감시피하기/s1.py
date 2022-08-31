import sys
sys.stdin = open('input.txt')

def look():
    visited = [[0] * n for _ in range(n)]
    for x, y in teachers:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 'O':
                    break
                if arr[nx][ny] == 'S':
                    return False
                nx += dx[i]
                ny += dy[i]
    return True

def find(cnt):
    global ans
    if cnt == 3:
        if look():
            ans = True
        return
    else:
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'X':
                    arr[i][j] = 'O'
                    find(cnt+1)
                    arr[i][j] = 'X'

input = sys.stdin.readline

n = int(input())
arr = []
students = []
teachers = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = False
for i in range(n):
    row = input().split()
    arr.append(row)
    for j in range(n):
        if arr[i][j] == 'S':
            students.append((i, j))
        elif arr[i][j] == 'T':
            teachers.append((i, j))
find(0)
if ans:
    print('YES')
else:
    print('NO')
