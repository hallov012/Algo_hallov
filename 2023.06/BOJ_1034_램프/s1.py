import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
print(arr)
k = int(input())
col_cnt = [0] * m
for j in range(m):
    for i in range(n):
        if arr[i][j] == '1':
            col_cnt[j] += 1
print(col_cnt)
