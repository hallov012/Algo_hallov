import sys
sys.stdin = open('input.txt')

r1, c1, r2, c2 = map(int, input().split())
arr = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
num = 1
d = 0
x, y = 0, 0
w = 1
cnt = 0
total = (c2-c1+1) * (r2-r1+1)
max_num = 0
while total > 0:
    if r1 <= x <= r2 and c1 <= y <= c2:
        total -= 1
        arr[x-r1][y-c1] = num
        max_num = num
    num += 1
    cnt += 1
    x += dx[d]
    y += dy[d]
    if cnt == w:
        cnt = 0
        d = (d+3) % 4
        if d == 0 or d == 2:
            w += 1
max_len = len(str(max_num))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(max_len), end=" ")
    print()

