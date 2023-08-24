import sys
sys.stdin = open('input.txt')

n = int(input())
ans = 0
for i in (14, 7, 1):
    if i > n:
        continue
    ans += n // i
    n %= i
    if not n:
        break
print(ans)