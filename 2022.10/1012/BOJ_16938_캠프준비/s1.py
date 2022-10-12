import sys
sys.stdin = open('input.txt')

def bfs(num, cnt, score, idx):
    global ans
    if score > r:
        return
    if cnt == num:
        arr = []
        for i in range(n):
            if visited[i]:
                arr.append(lvs[i])
        if l <= sum(arr) <= r and max(arr) - min(arr) >= x:
            ans += 1
    for i in range(idx+1, n):
        if not visited[i]:
            visited[i] = 1
            bfs(num, cnt+1, score+lvs[i], i)
            visited[i] = 0

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
lvs = list(map(int, input().split()))

ans = 0
for i in range(2, n+1):
    visited = [0] * n
    bfs(i, 0, 0, -1)
print(ans)