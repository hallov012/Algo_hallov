import sys
sys.stdin = open('input.txt')

def cut(n, x, y):
    global ans
    if n == 1:
        ans[arr[x][y]] += 1
        return

    m = n // 2
    # 우상단, 좌상단, 우하단, 좌하단
    sum_lst = [0] * 4
    edges = [(x, y), (x, y + m), (x + m, y), (x + m, y + m)]
    sum_lst[0] = sum(sum(arr[i][y: y + m]) for i in range(x, x + m))
    sum_lst[1] = sum(sum(arr[i][y + m: y + 2 * m]) for i in range(x, x + m))
    sum_lst[2] = sum(sum(arr[i][y: y + m]) for i in range(x + m, x + 2 * m))
    sum_lst[3] = sum(sum(arr[i][y + m: y + m * 2]) for i in range(x + m, x + m * 2))

    for i in range(4):
        if sum_lst[i] == 0:
            ans[0] += 1
        elif sum_lst[i] == m*m:
            ans[1] += 1
        else:
            cut(m, edges[i][0], edges[i][1])

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# idx 0 => 흰색, 1 => 파란색
ans = [0, 0]
blue_cnt = sum([sum(line) for line in arr])
if blue_cnt == 0:
    print(1)
    print(0)
    exit()
elif blue_cnt == n*n:
    print(0)
    print(1)
    exit()

cut(n, 0, 0)

print(ans[0])
print(ans[1])
