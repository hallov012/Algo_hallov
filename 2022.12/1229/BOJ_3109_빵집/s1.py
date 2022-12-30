import sys
sys.stdin = open('input.txt')

def find(x, y):
    if y == c-1:
        return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r:
            if arr[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = 1
                if find(nx, ny):
                    return True
    return False

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [input().rstrip() for _ in range(r)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
visited = [[0] * c for _ in range(r)]
ans = 0
for i in range(r):
    if arr[i][0] == '.':
        if find(i, 0):
            ans += 1
print(ans)