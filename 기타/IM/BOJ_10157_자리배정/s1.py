import sys
sys.stdin = open('input.txt')

c, r = map(int, input().split())
k = int(input())
arr = [[0] * c for _ in range(r)]
# 경기장을 아래로 뒤집어서 넘버링 (1,1) -> (0, 0) 출력할 떄 +1 씩 해주기
# 이동방향은 아래, 오른쪽, 위, 왼쪽
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
i, j = 0, 0
n = 1
d = 0
if k > c * r:
    print(0)
else:
    while 1:
        arr[i][j] = n
        if n == k:
            break
        if i + dr[d] in range(r) and j + dc[d] in range(c) and not arr[i+dr[d]][j+dc[d]]:
            pass
        else:
            d = (d + 1) % 4
        i += dr[d]
        j += dc[d]
        n += 1
    print(j+1, i+1)


