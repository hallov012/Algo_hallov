# 2차원누적합 => 공부 필요
import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
bw_arr = [[0] * (m+1) for _ in range(n+1)]
odd_line = "BW" * (m//2)
even_line = "WB" * (m//2)

if m % 2:
    odd_line += "B"
    even_line += "W"

for i in range(n):
    if i % 2:
        for j in range(m):
            bw_arr[i][j] = bw_arr[i-1][j] + bw_arr[i][j-1] - bw_arr[i-1][j-1]
            if arr[i][j] != even_line[j]:
                bw_arr[i][j] += 1
    else:
        for j in range(m):
            bw_arr[i][j] = bw_arr[i-1][j] + bw_arr[i][j-1] - bw_arr[i-1][j-1]
            if arr[i][j] != odd_line[j]:
                bw_arr[i][j] += 1

ans = sys.maxsize
for i in range(n-k+1):
    for j in range(m-k+1):
        temp = bw_arr[i+k-1][j+k-1] + bw_arr[i-1][j-1] - bw_arr[i+k-1][j-1] - bw_arr[i-1][j+k-1]
        ans = min(ans, temp, k*k-temp)
print(ans)


