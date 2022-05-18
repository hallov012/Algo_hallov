import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, h = map(int, input().split())
arr = [0] * h
ans = [n, 0]
for i in range(1, n+1):
    m = int(input())
    if i % 2:
        for j in range(h-1, h-1-m, -1):
            arr[j] += 1
    else:
        for j in range(m):
            arr[j] += 1

ans = [n, 0]
for num in arr:
    if num < ans[0]:
        ans = [num, 1]
    elif num == ans[0]:
        ans[1] += 1

print(*ans)
