import sys
sys.stdin = open('input.txt')

def cut(n, x, y):
    if n == 1:
        ans[arr[x][y]] += 1
        return
    m = n // 2
    for i in range(2):
        x1, x2 = x + m*i, x + m*(i+1)
        for j in range(2):
            y1, y2 = y + m*j, y + m*(j+1)
            start = arr[x1][y1]
            flag = True
            for a in range(x1, x2):
                for b in range(y1, y2):
                    if arr[a][b] != start:
                        flag = False
                        break
            if flag:
                ans[start] += 1
            else:
                cut(m, x1, y1)

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue_cnt = sum(sum(line) for line in arr)

# idx 0 => 흰색, 1 => 파란색
ans = [0, 0]
if blue_cnt == 0:
    ans[0] += 1
elif blue_cnt == n*n:
    ans[1] += 1
else:
    cut(n, 0, 0)

print(ans[0])
print(ans[1])
