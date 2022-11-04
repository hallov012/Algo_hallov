import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = 9
data = [list(map(int, input().split())) for _ in range(n)]
max_num = 0
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] > max_num:
            ans = [i+1, j+1]
            max_num = data[i][j]
print(max_num)
print(*ans)