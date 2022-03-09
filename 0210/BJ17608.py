import sys

n = int(sys.stdin.readline())

data = []
for _ in range(n):
    h = int(sys.stdin.readline())
    data.append(h)

cnt = 0
top = 0
for i in reversed(range(n)):
    if data[i] > top :
        top = data[i]
        cnt += 1

print(cnt)
