import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == 'S':
                        print(0)
                        exit()
        elif arr[i][j] == '.':
            arr[i][j] = 'D'

print(1)
for line in arr:
    print(''.join(line))


