import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
ans = 0
for _ in range(n):
    str = input().split("-")
    if int(str[1]) <= 90:
        ans += 1
print(ans)