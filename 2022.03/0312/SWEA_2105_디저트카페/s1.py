import sys
sys.stdin = open('input.txt')

def go(x, y):
    dessert = []
    for _ in range(a):
        x += dx[0]
        y += dy[0]
        if 0 <= x < n and 0 <= y < n:
            if cafe[x][y] not in dessert:
                dessert.append(cafe[x][y])
            else:
                return []
        else:
            return []
    for _ in range(b):
        x += dx[1]
        y += dy[1]
        if 0 <= x < n and 0 <= y < n:
            if cafe[x][y] not in dessert:
                dessert.append(cafe[x][y])
            else:
                return []
        else:
            return []
    for _ in range(a):
        x += dx[2]
        y += dy[2]
        if 0 <= x < n and 0 <= y < n:
            if cafe[x][y] not in dessert:
                dessert.append(cafe[x][y])
            else:
                return []
        else:
            return []
    for _ in range(b):
        x += dx[3]
        y += dy[3]
        if 0 <= x < n and 0 <= y < n:
            if cafe[x][y] not in dessert:
                dessert.append(cafe[x][y])
            else:
                return []
        else:
            return []
    return dessert

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, -1, 1]
    dy = [1, 1, -1, -1]
    ans = -1
    for x in range(n):
        for y in range(n):
            for a in range(1, n):
                for b in range(1, n):
                    dessert_num = len(go(x, y))
                    if dessert_num > 0:
                        ans = max(ans, dessert_num)
    print(f'#{tc} {ans}')

