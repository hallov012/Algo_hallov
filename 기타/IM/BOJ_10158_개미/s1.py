import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

dr = [1, 1, -1, 1]
dc = [1, -1, -1, -1]
i, j = q, p
d = 0
time = 0
while time < t:
    if i + dr[d] in range(h+1) and j + dc[d] in range(w+1):
        pass
    elif i + dr[d] not in range(h+1) and j + dc[d] not in range(w+1):
        d = (d + 2) % 4
    else:
        d = (d + 1) % 4
    i += dr[d]
    j += dc[d]
    time += 1
print(j, i)


