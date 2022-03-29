import sys
sys.stdin = open('input.txt')

def find(i, end_time, cnt):
    global ans
    if i == n-1:
        ans = max(ans, cnt)
    for j in range(i, n):
        if data[j][0] >= end_time:
            find(j, data[j][1], cnt + 1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort()
    ans = 1
    find(0, 0, 0)
    print(f'#{tc} {ans}')