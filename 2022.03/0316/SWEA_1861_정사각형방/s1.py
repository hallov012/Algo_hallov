import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_cnt = 0
    ans = []
    for i in range(n):
        for j in range(n):
            visited = [[0] * n for _ in range(n)]
            cnt = 1
            que = [[i, j]]
            visited[i][j] = 1
            while que:
                x, y = que.pop(0)
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if room[nx][ny] == room[x][y] + 1 and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            cnt += 1
                            que.append([nx, ny])
            if cnt > max_cnt:
                max_cnt = cnt
                ans = [[i, j]]
            elif cnt == max_cnt:
                ans.append([i, j])
    max_room = []
    print(f'#{tc}', end=' ')
    if len(ans) == 1:
        print(room[ans[0][0]][ans[0][1]], end=' ')
        print(max_cnt, end=' ')
    else:
        for idx in ans:
            max_room.append(room[idx[0]][idx[1]])
        print(min(max_room), end=' ')
        print(max_cnt, end=' ')
    print()