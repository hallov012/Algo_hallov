import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))
visited = [0] * n
que = deque([0])
visited[0] = 1
while que:
    x = que.popleft()
    if arr[x]:
        for i in range(1, arr[x]+1):
            if x+i < n and not visited[x+i]:
                visited[x+i] = visited[x] + 1
                que.append(x+i)
print(visited[-1]-1)
