import sys
sys.stdin = open('input.txt')

def game(x, y):
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    cnt = 1
    while True:
        m, d = int(arr[x][y][:-1]), arr[x][y][-1]
        while m:
            x += direction[d][0]
            y += direction[d][1]
            if x < 0 or x >= n:
                x %= n
            if y < 0 or y >= n:
                y %= n
            if not visited[x][y]:
                visited[x][y] = 1
                cnt += 1
                m -= 1
            else:
                return cnt

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
arr = [input().split() for _ in range(n)]
direction = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

g_cnt = game(x1-1, y1-1)
p_cnt = game(x2-1, y2-1)

if g_cnt > p_cnt:
    print("goorm", g_cnt)
else:
    print("player", p_cnt)