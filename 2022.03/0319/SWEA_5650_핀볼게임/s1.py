import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]  # 0: 상, 1: 하, 2: 좌, 3:
    dy = [0, 0, -1, 1]
    block_lst = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0], [1, 0, 3, 2]]
    hole_dic = {}
    ans = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 5:
                if arr[i][j] not in hole_dic.keys():
                    hole_dic[arr[i][j]] = [[i, j]]
                else:
                    hole_dic[arr[i][j]].append([i, j])
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 0:
                for k in range(4):
                    cnt = 0
                    x, y, d = a, b, k
                    while 1:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        # 범위 밖으로 나갔을 때, 반대 방향으로 다시 돌려줌
                        if nx in [-1, n] or ny in [-1, n]:
                            if nx == -1:
                                d = 1
                                nx = 0
                            elif nx == n:
                                d = 0
                                nx = n - 1
                            elif ny == -1:
                                d = 3
                                ny = 0
                            elif ny == n:
                                d = 2
                                ny = n - 1
                            cnt += 1
                        # block을 마주쳤을 때
                        if 0 < arr[nx][ny] < 6:
                            d = block_lst[arr[nx][ny]][d]
                            cnt += 1
                        # 웜홀을 마주쳤을 때
                        elif 5 < arr[nx][ny]:
                            for hole in hole_dic[arr[nx][ny]]:
                                if hole != [nx, ny]:
                                    nx, ny = hole[0], hole[1]
                                    break
                        if arr[nx][ny] == -1 or (nx == a and ny == b):
                            break
                        x, y = nx, ny
                    ans = max(ans, cnt)
    print(f'#{tc} {ans}')





