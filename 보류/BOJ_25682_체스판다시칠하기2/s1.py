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
    # WBWBWB 순서
    if i % 2:
        for j in range(m):
            if arr[i][j] != even_line[j]:
                bw_arr[i+1][j+1] += 1
            bw_arr[i+1][j+1] += bw_arr[i+1][j]
    else:
        for j in range(m):
            if arr[i][j] != odd_line[j]:
                bw_arr[i+1][j+1] += 1
            bw_arr[i+1][j+1] += bw_arr[i+1][j]
    bw_arr[i+1][j+1] += bw_arr[i][j+1]

print(bw_arr)

ans = sys.maxsize
for i in range(n-k+1):
    for j in range(m-k+1):
        temp = bw_arr[i+k][j+k] - bw_arr[i][j]
        ans = min(ans, temp, k*k-temp)
print(ans)
