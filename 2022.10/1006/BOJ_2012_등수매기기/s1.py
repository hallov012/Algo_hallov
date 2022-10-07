import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

ans = 0
for i in range(1, n+1):
    ans += abs(i - data[i-1])
print(ans)