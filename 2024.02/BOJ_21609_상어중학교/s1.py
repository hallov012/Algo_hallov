import sys, heapq
from collections import deque
sys.stdin = open('input.txt')

def find_group():
    block_list = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt, block = bfs(i, j)
                heapq.heappush(block_list, (-cnt, block))
    return block_list


def bfs(a, b):
    c = arr[a][b]
    visited[a][b] = 1
    que = deque([(a, b)])
    block = [(a, b)]
    cnt = 1
    r_cnt = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 무지개는 여기저기 사용될 수 있긴 한데, 한번의 시도에서는 한번만 사용되는거니까 그거 visited 체크 해야함
                # 몇번째 블록인지 idx를 받아서 그걸로 예외처리 하는 방법을 생각해보자
                if (arr[nx][ny] == c and not visited[nx][ny]) or arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                    block.append((nx, ny))
                    if arr[nx][ny] == 0:
                        r_cnt += 1
    return cnt, block

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

"""
-1: 검은색, 무지개: 0
블록 그룹: 연결된 블록의 그룹이며 검은색은 있으면 안되고, 일반 블록이 1개는 있어야하며 색이 모두 같아야 함, 크기는 2 이상
기준 블록: 블록 그룹에서 무지개색이 아니면서 좌상단에 있는 블록
"""

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    visited = [[0] * n for _ in range(n)]
    blocks = find_group()
    print(blocks)
    break



