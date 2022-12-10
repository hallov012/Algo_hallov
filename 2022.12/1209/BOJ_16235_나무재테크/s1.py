import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n, m, k = map(int, input().split())
add = [list(map(int, input().split())) for _ in range(n)]
arr = [[5] * n for _ in range(n)]
trees = []
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees.append((x-1, y-1, z))
while k > 0:
    # 어린 나무가 먼저 성장해야하므로 나이순으로 정렬
    trees.sort(key=lambda x:x[2])
    live = []
    die = []
    # 봄
    for x, y, z in trees:
        if arr[x][y] >= z:
            arr[x][y] -= z
            z += 1
            live.append((x, y, z))
        else:
            die.append((x, y, z))

    # 여름
    for x, y, z in die:
        arr[x][y] += z // 2

    # 가을
    for x, y, z in live:
        if not z % 5:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    live.append((nx, ny, 1))

    # 겨울
    for i in range(n):
        for j in range(n):
            arr[i][j] += add[i][j]

    trees = live
    k -= 1

print(len(trees))

