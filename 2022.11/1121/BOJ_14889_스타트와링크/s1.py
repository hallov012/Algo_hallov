import sys
sys.stdin = open('input.txt')

def check(arr):
    cnt = 0
    for i in range(n//2):
        for j in range(n//2):
            cnt += data[arr[i]][arr[j]]
    return cnt

def find(cnt, idx):
    global ans
    if cnt == n//2:
        team1 = []
        team2 = []
        for j in range(n):
            if visited[j]:
                team1.append(j)
            else:
                team2.append(j)
        temp = abs(check(team1) - check(team2))
        ans = min(ans, temp)
        return
    for i in range(idx+1, n):
        if not visited[i]:
            visited[i] = 1
            find(cnt+1, i)
            visited[i] = 0

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = sys.maxsize
find(0, -1)
print(ans)
