import sys, copy
from collections import deque

sys.stdin = open('input.txt')

def break_block(j, data):
    hit = []
    for i in range(h):
        if data[i][j] > 0:
            hit = [i, j]
            break
    if not hit:    # 해당 행에 벽돌이 남아있지 않으면 return
        return
    break_position = [[0] * w for _ in range(h)]
    que = deque([hit])
    break_position[hit[0]][hit[1]] = 1
    while que:
        x, y = que.popleft()
        n = data[x][y]
        if n > 1:
            for d in range(4):
                for a in range(1, n):
                    nx = x + dx[d] * a
                    ny = y + dy[d] * a
                    if 0 <= nx < h and 0 <= ny < w:
                        if not break_position[nx][ny] and data[nx][ny] > 0:
                            break_position[nx][ny] = 1
                            que.append([nx, ny])
    copy_data = copy.deepcopy(data)
    for j in range(w):
        check = False
        l = h
        for b in range(h-1, -1, -1):
            if check:               # 위에 남은 모든 행을 0으로 바꿔줌 (더 이상 블록이 없다)
                data[b][j] = 0
            else:
                if not l:           # 모든 행을 댜 봤을 때, 남은 칸은 0으로 채워준다
                    check = True
                else:
                    l -= 1
                    while break_position[l][j]:  # 깨지지 않은 벽돌이 나올 떄 까지
                        l -= 1
                        if l < 0:                # 만약 모든 행을 다 봤다면, check 를 갱신
                            check = True
                            break
                    if copy_data[l][j] > 0:      # 블록이 있을 때
                        data[b][j] = copy_data[l][j]   # 블록 값으로 저장
                    elif copy_data[l][j] == 0:   # 쌓여있는 블록을 모두 보았을 떄, check 를 갱신
                        check = True
                if check:
                    data[b][j] = 0
    return

def position(ball, data):
    global ans
    copy_data = copy.deepcopy(data)
    if ball == n:
        cnt = 0
        for a in range(h):
            for b in range(w):
                if data[a][b] > 0:
                    cnt += 1
        ans = min(ans, cnt)
        return
    for j in range(w):
        break_block(j, copy_data)
        position(ball + 1, copy_data)
        copy_data = copy.deepcopy(data)


T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    block = []
    for _ in range(h):
        data = list(map(int, input().split()))
        block.append(data)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = w * h
    position(0, block)
    print(f'#{tc} {ans}')


