import sys
sys.stdin = open('input.txt')

def bfs(loss, cnt):
    global ans
    if loss <= k:
        ans = max(ans, cnt)
        if ans == sum(p_lst):
            print(ans)
            exit()
    else:
        return
    for i in range(n):
        if not visited[i]:
            now_loss = loss + a_lst[i]
            visited[i] = 1
            bfs(loss + now_loss, cnt + p_lst[i])
            visited[i] = 0

n, k = map(int, input().split())
a_lst = list(map(int, input().split()))
p_lst = list(map(int, input().split()))
visited = [0] * n
ans = 0
bfs(0, 0)
print(ans)