import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
max_ans = data[0]
min_ans = data[0]

for i in range(1, n):
    max_ans = [max(max_ans[0], max_ans[1]) + data[i][0],
        max(max_ans[0], max_ans[1], max_ans[2]) + data[i][1],
        max(max_ans[1], max_ans[2]) + data[i][2]]

    min_ans = [min(min_ans[0], min_ans[1]) + data[i][0],
        min(min_ans[0], min_ans[1], min_ans[2]) + data[i][1],
        min(min_ans[1], min_ans[2]) + data[i][2]]

print(max(max_ans), min(min_ans))