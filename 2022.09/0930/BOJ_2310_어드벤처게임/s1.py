import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def dfs(now, money):
    global ans
    if rooms[now-1][0] == 'L':
        if money < int(rooms[now-1][1]):
            money = int(rooms[now-1][1])
    elif rooms[now-1][0] == 'T':
        money -= int(rooms[now-1][1])
        if money < 0:
            return
    if now == n:
        ans = True
        return
    for i in range(2, len(rooms[now-1])-1):
        next = int(rooms[now-1][i])
        if not visited[next]:
            visited[next] = 1
            dfs(next, money)
            visited[next] = 0

while True:
    n = int(input())
    if not n:
        break
    rooms = [list(input().split()) for _ in range(n)]
    visited = [0] * (n+1)
    visited[1] = 1
    ans = False
    dfs(1, 0)
    if ans:
        print('Yes')
    else:
        print('No')
