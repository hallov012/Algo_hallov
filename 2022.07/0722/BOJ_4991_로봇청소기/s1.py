import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt')

def bfs(a, b):
    visited = [[0] * w for _ in range(h)]
    visited[a][b] = 1
    que = deque([(a, b)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and data[nx][ny] != 'x':
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    return visited

input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    data = []
    dust = []
    for i in range(h):
        line = input()
        data.append(line)
        for j in range(w):
            if line[j] == 'o':
                sx, sy = i, j
            elif line[j] == '*':
                dust.append((i, j))

    # 시작 지점부터 모든 먼지까지의 최단거리를 구한다
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    from_start_visited = bfs(sx, sy)

    flag = True
    from_start_d = []
    for x, y in dust:
        if not from_start_visited[x][y]:
            flag = False
            break
        else:
            from_start_d.append(from_start_visited[x][y]-1)
    # 먼지가 있는 곳을 방문할 수 없는 것 이므로 종료
    if not flag:
        print(-1)
        continue

    # 먼지와 먼지 사이의 거리를 distance에 이차원배열의 형태로 저장
    distance = [[0] * len(dust) for _ in range(len(dust))]
    for i in range(len(dust)-1):
        x, y = dust[i]
        dust_to_dust = bfs(x, y)
        for j in range(i+1, len(dust)):
            nx, ny = dust[j]
            distance[i][j] = dust_to_dust[nx][ny]-1
            distance[j][i] = distance[i][j]

    # 순열을 이용해 모든 경로를 계산해본다
    ans = sys.maxsize
    path = list(permutations(range(len(dust))))
    for case in path:
        cnt = 0
        cnt += from_start_d[case[0]]
        start = case[0]
        for j in range(1, len(case)):
            end = case[j]
            cnt += distance[start][end]
            start = end
        ans = min(ans, cnt)

    print(ans)