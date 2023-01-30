import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
arr = [input().rstrip() for _ in range(n)]
data = [list(map(int, input().split())) for _ in range(k)]
add_sum = [[[0, 0, 0] for _ in range(m+1)] for _ in range(n+1)]
pare = {'J': 0, 'O': 1, 'I': 2}

for i in range(n):
    for j in range(m):
        for l in range(3):
            add_sum[i+1][j+1][l] = add_sum[i+1][j][l] + add_sum[i][j+1][l] - add_sum[i][j][l]
        add_sum[i+1][j+1][pare[arr[i][j]]] += 1

for x1, y1, x2, y2 in data:
    ans = [0, 0, 0]
    for i in range(3):
        ans[i] = add_sum[x2][y2][i] - add_sum[x1-1][y2][i] - add_sum[x2][y1-1][i] + add_sum[x1-1][y1-1][i]
    print(*ans)