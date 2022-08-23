import sys
sys.stdin = open('input.txt')

def rotate(dir):
    if dir == 0: # 동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 1: # 서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2: # 북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif dir == 3: # 남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))
dice = [0] * 6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for dir in direction:
    dir -= 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m:
        rotate(dir)
        print(dice[0])
        x, y = nx, ny
        if arr[x][y]:
            dice[5] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[5]
