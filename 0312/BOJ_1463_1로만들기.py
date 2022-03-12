from collections import deque

n = int(input())

min_ans = 10 ** 6
que = deque([[n, 0]])
visited = [0] * (n+1)
visited[n] = 1
while que:
    num, cnt = que.popleft()
    if num == 1:
        break
    if not visited[num-1]:
        visited[num-1] = 1
        que.append([num-1, cnt+1])
    if not num % 3:
        if not visited[num//3]:
            visited[num//3] = 1
            que.append([num//3, cnt+1])
    if not num % 2:
        if not visited[num//2]:
            visited[num//2] = 1
            que.append([num//2, cnt+1])

print(cnt)