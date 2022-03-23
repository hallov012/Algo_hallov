import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    left = [True] * k
    micros = []
    for q in range(k):
        micro = list(map(int, input().split()))
        arr[micro[0]][micro[1]] = 1
        micros.append(micro)

    while m > 0:
        check_point = []
        for i in range(k):
            if left[i]:  # 군집이 사라지지 않았을 때
                x, y, cnt, d = micros[i]
                nx = x + dx[d]
                ny = y + dy[d]
                # 약품이 칠해진 공간으로 이동했을 때
                if nx == 0:
                    cnt //= 2
                    d = 2
                elif nx == n-1:
                    cnt //= 2
                    d = 1
                elif ny == 0:
                    cnt //= 2
                    d = 4
                elif ny == n-1:
                    cnt //= 2
                    d = 3
                arr[x][y] -= 1
                arr[nx][ny] += 1
                if arr[nx][ny] > 1:
                    check_point.append([nx, ny])
                if cnt == 0:
                    left[i] = False
                micros[i] = [nx, ny, cnt, d]
        if check_point:
            for point in check_point:
                merge_cnt = []
                merge_idx = []
                for j in range(k):
                    if left[j]:
                        if micros[j][0] == point[0] and micros[j][1] == point[1]:
                            merge_cnt.append(micros[j][2])
                            merge_idx.append(j)
                if len(merge_idx) > 1:
                    for l in range(len(merge_idx)):
                        if merge_cnt[l] == max(merge_cnt):
                            micros[merge_idx[l]][2] = sum(merge_cnt)
                        else:
                            micros[merge_idx[l]][2] = 0
                            left[merge_idx[l]] = False
        m -= 1
    ans = 0
    for micro in micros:
        ans += micro[2]

    print(f'#{tc} {ans}')


