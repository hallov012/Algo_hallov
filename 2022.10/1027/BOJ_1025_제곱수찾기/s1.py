import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m = map(int,  input().split())
arr = [list(input().strip()) for _ in range(n)]
ans = -1

for i in range(n):
    for j in range(m):
        for xd in range(-n, n):
            for yd in range(-m ,m):
                temp = ""
                x, y = i, j
                if not xd and not yd:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    temp += arr[x][y]
                    if int(temp) ** 0.5 == int(int(temp) ** 0.5) :
                        ans = max(ans, int(temp))
                    x += xd
                    y += yd
print(ans)

