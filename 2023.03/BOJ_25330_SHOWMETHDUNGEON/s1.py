import sys
sys.stdin = open('input.txt')

def bfs(loss, sum_a, cnt):
    global ans
    if loss <= k:
        ans = max(ans, cnt)
        if ans == total_p:
            print(ans)
            exit()
    else:
        return
    temp = cnt
    for i in range(n):
        if not visited[i] and a[i] <= k - loss:
            temp += p[i]
    if temp <= ans:
        return
    for i in range(n):
        if not visited[i]:
            now_loss = sum_a + a[i]
            visited[i] = 1
            bfs(loss + now_loss, sum_a + a[i], cnt + p[i])
            visited[i] = 0

n, k = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
total_p = sum(p)
visited = [0] * n
ans = 0
bfs(0, 0, 0)
print(ans)
