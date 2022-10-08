import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
ans = 0
if n == 1:
    print(data[0])
    exit()
for i in range(0, n-1, 2):
    now, next = data[i], data[i+1]
    if now < 0 and next < 0:
        ans += now * next
    else:
        if now < 0 and next > 0:
            ans += now
        break
if i+2 == n-1:
    if data[-1] < 0:
        ans += data[-1]
idx = 0
for i in range(n-1, 0, -2):
    now, next = data[i], data[i-1]
    if now > 1 and next > 1:
        ans += now * next
    else:
        idx = i
        break
for i in range(idx, -1, -1):
    if data[i] >= 0:
        ans += data[i]
    else:
        break
print(ans)