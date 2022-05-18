import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, h = map(int, input().split())
top = [0] * (h+1)
bottom = [0] * (h+1)
ans = [n, 0]

for i in range(n):
    m = int(input())
    if i % 2:
        top[m] += 1
    else:
        bottom[m] += 1

for i in range(h-1, 0, -1):
    top[i] += top[i+1]
    bottom[i] += bottom[i+1]

for i in range(1, h+1):
    num = top[i] + bottom[h-i+1]
    if num < ans[0]:
        ans = [num, 1]
    elif num == ans[0]:
        ans[1] += 1

print(*ans)