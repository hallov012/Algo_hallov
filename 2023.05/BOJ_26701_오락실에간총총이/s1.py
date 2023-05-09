import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

min_x = min_y = n
max_x = max_y = -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

ans = 0
if min_x != max_x:
    ans += min(max_x, n-1-min_x)
if min_y != max_y:
    ans += min(max_y, n-1-min_y)
print(ans)