import sys
sys.stdin = open('input.txt')

def find(cnt, now):
    global ans
    if len(now) == 1:
        ans = min(ans, cnt)
    if cnt >= ans:
        return
    for i in range(4):
        new = set()
        for x, y in now:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new.add((nx, ny))
            else:
                new.add((x, y))
        find(cnt+1, new)

input = sys.stdin.readline

n = int(input())
arr = []
goms = set()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    line = input().rstrip()
    arr.append(line)
    for j in range(n):
        if line[j] == "G":
            goms.add((i, j))
ans = sys.maxsize
find(0, goms)
print(ans)