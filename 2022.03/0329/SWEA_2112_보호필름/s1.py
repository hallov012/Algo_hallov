import sys
sys.stdin = open('input.txt')

def check(data):
    for j in range(w):
        ch = False
        i = 0
        cnt = 1
        while i + 1 < d:
            if data[i][j] == data[i+1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt == k:
                ch = True
                break
            i += 1
        if not ch:
            return False
    return True

def find(cnt, film, n):
    global ans
    if cnt >= ans:
        return
    if check(film):
        ans = min(ans, cnt)
        return
    for i in range(n, d):
        if not visited[i]:
            save = film[i][:]
            visited[i] = 1
            film[i] = [0] * w
            find(cnt + 1, film, i)
            film[i] = [1] * w
            find(cnt + 1, film, i)
            film[i] = save
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    if k == 1:
        ans = 0
    else:
        visited = [0] * d
        ans = k
        find(0, film, 0)
    print(f'#{tc} {ans}')