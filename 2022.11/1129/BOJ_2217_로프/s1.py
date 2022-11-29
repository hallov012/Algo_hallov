import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
ans = 0
for i in range(n):
    temp = data[i] * (i+1)
    if temp > ans:
        ans = temp
print(ans)