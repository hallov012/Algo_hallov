import sys, heapq
from collections import deque
sys.stdin = open('input.txt')

def find_group():
    block_list = []
    idx = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                block, r_block = bfs(i, j, idx)
                c_cnt, r_cnt = len(block), len(r_block)
                heapq.heappush(block_list, (-(c_cnt + r_cnt), -r_cnt, block, r_block))
                idx += 1
    return block_list

def bfs(a, b, idx):
    c = arr[a][b]
    visited[a][b] = idx
    que = deque([(a, b)])
    block = [(-a, -b)]
    r_block = []
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if (arr[nx][ny] == c or arr[nx][ny] == 0) and visited[nx][ny] != idx:
                    visited[nx][ny] = idx
                    que.append((nx, ny))
                    if arr[nx][ny] == 0:
                        r_block.append((nx, ny))
                    else:
                        heapq.heappush(block, (-nx, -ny))

    return block, r_block

def gravity():
    for j in range(n):
        for i in range(n-1, -1, -1):
            if arr[i][j] != empty and arr[i][j] != -1:
                idx = i+1
                while idx < n and arr[idx][j] == empty:
                    idx += 1
                if idx-1 != i:
                    arr[idx-1][j] = arr[i][j]
                    arr[i][j] = empty

def rotate_board():
    new_arr = [[-2] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_arr[n-j-1][i] = arr[i][j]
    return new_arr

def check_game_end():
    if not blocks:
        return True
    if blocks[0][0] > -2:
        return True
    return False

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

"""
-1: 검은색, 무지개: 0
블록 그룹: 연결된 블록의 그룹이며 검은색은 있으면 안되고, 일반 블록이 1개는 있어야하며 색이 모두 같아야 함, 크기는 2 이상
기준 블록: 블록 그룹에서 무지개색이 아니면서 좌상단에 있는 블록
"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
empty = -2
ans = 0

while True:
    visited = [[0] * n for _ in range(n)]
    blocks = find_group()
    print(blocks)
    if check_game_end():
        break

    cnt, location, r_location = blocks[0][0], blocks[0][2], blocks[0][3]
    ans += cnt ** 2
    for x, y in location:
        arr[-x][-y] = empty
    for x, y in r_location:
        arr[x][y] = empty
    gravity()
    arr = rotate_board()
    gravity()

print(ans)





