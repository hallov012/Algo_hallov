import sys
sys.stdin = open('input.txt')

def dfs(x, y, word):
    if len(word) == 7:
        ans.add(word)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, word + data[nx][ny])

T = int(input())

for tc in range(1, T+1):
    data = [input().split() for _ in range(4)]
    ans = set()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        for j in range(4):
            word = data[i][j]
            dfs(i, j, word)
    print(f'#{tc} {len(ans)}')